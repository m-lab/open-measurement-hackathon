#!/usr/bin/env python3

import os
import json
from pytricia import PyTricia
from neo4j import GraphDatabase

URI = 'neo4j://sandbox.ihr.live:7687'
AUTH = None
OUTPUT_FOLDER = "data"
OUTPUT_FILE_PREFIX = "sibling_ips"

class SiblingPrefixesHashTable():
    def __init__(self):
        spv4_file = os.path.join(OUTPUT_FOLDER, f"{OUTPUT_FILE_PREFIX}_v4.jsonl")
        spv6_file = os.path.join(OUTPUT_FOLDER, f"{OUTPUT_FILE_PREFIX}_v6.jsonl")

        if not os.path.exists(spv4_file) and not os.path.exists(spv6_file):
            v4, v6 = self._get_sibling_prefixes()
            print(f"[LOG] Total IPv4 Sibling Source Prefixes: {len(v4):,}")
            print(f"[LOG] Total IPv6 Sibling Source Prefixes: {len(v6):,}")
            export_sibling_prefixes(v4, spv4_file)
            export_sibling_prefixes(v6, spv6_file)
        else:
            print(f"[LOG] Files already exist. Won't query, just load.")
        
        self.sibling_prefixes_v4 = read_sibling_prefixes(spv4_file)
        self.sibling_prefixes_v6 = read_sibling_prefixes(spv6_file)

        sibling_prefixes_tree_v4, sibling_prefixes_tree_v6 = self._construct_hash_tree(self.sibling_prefixes_v4, self.sibling_prefixes_v6)
        self.table = {
            '4': sibling_prefixes_tree_v4,
            '6': sibling_prefixes_tree_v6
        }
        print(f"[LOG] Tables are constructed.")
    
    def lookup(self, addr):
        return (self.table['4'].get_key(addr), self.table['4'].get(addr)) if '.' in addr else (self.table['6'].get_key(addr), self.table['6'].get(addr))

    def _get_sibling_prefixes(self):
        db = GraphDatabase.driver(URI, auth=AUTH)

        db.verify_connectivity()

        records, _, _ = db.execute_query(
            """
            MATCH (ip4:IP {af:4})-[:ASSIGNED]-(x:AtlasProbe)-[:ASSIGNED]-(ip6:IP {af:6})
            WHERE x.status_name = 'Connected'
            MATCH (ip4)-[:PART_OF]-(p4:BGPPrefix)
            MATCH (ip6)-[:PART_OF]-(p6:BGPPrefix)
            MATCH (a4:AS)-[r4:ORIGINATE {reference_org: "BGPKIT"}]-(p4)
            MATCH (a6:AS)-[r6:ORIGINATE {reference_org: "BGPKIT"}]-(p6)
            WHERE (p6.prefix <> '::/0' AND p4.prefix <> '0.0.0.0/0')
            ORDER BY p4.network, p4.prefixlen, p6.network, p6.prefixlen
            RETURN DISTINCT x.id as probe_id, a4.asn as v4_asn, a6.asn as v6_asn, ip4.ip as v4_ip, p4.prefix as v4_prefix, ip6.ip as v6_ip, p6.prefix as v6_prefix
            """
        )

        sibling_prefixes_v4 = {}
        sibling_prefixes_v6 = {}
        for r in records:
            if r["v4_prefix"] not in sibling_prefixes_v4:
                sibling_prefixes_v4[r["v4_prefix"]] = set()
            sibling_prefixes_v4[r["v4_prefix"]].add(r["v6_ip"])
            if r["v6_prefix"] not in sibling_prefixes_v6:
                sibling_prefixes_v6[r["v6_prefix"]] = set()
            sibling_prefixes_v6[r["v6_prefix"]].add(r["v4_ip"])

        db.close()

        for prefix in sibling_prefixes_v4:
            v6_siblings = sorted(list(sibling_prefixes_v4[prefix]))
            sibling_tree = PyTricia(128)
            for sibling in v6_siblings:
                if sibling not in sibling_tree:
                    sibling_tree.insert(sibling, 0)
            v6_less_specific_siblings = list(sibling_tree.keys())
            sibling_prefixes_v4[prefix] = v6_less_specific_siblings

        for prefix in sibling_prefixes_v6:
            v4_siblings = sorted(list(sibling_prefixes_v6[prefix]))
            sibling_tree = PyTricia(32)
            for sibling in v4_siblings:
                if sibling not in sibling_tree:
                    sibling_tree.insert(sibling, 0)
            v4_less_specific_siblings = list(sibling_tree.keys())
            sibling_prefixes_v6[prefix] = v4_less_specific_siblings

        sibling_prefixes_v4 = dict(sorted(sibling_prefixes_v4.items(), key=lambda x: int(x[0].split("/")[-1])))
        sibling_prefixes_v6 = dict(sorted(sibling_prefixes_v6.items(), key=lambda x: int(x[0].split("/")[-1])))
        
        return sibling_prefixes_v4, sibling_prefixes_v6

    def _construct_hash_tree(self, sibling_prefixes_v4, sibling_prefixes_v6):
        sibling_prefixes_tree_v4 = PyTricia(32)
        for prefix in sorted(sibling_prefixes_v4):
            sibling_prefixes_tree_v4.insert(prefix, sibling_prefixes_v4[prefix])

        sibling_prefixes_tree_v6 = PyTricia(128)
        for prefix in sorted(sibling_prefixes_v6):
            sibling_prefixes_tree_v6.insert(prefix, sibling_prefixes_v6[prefix])
        
        return sibling_prefixes_tree_v4, sibling_prefixes_tree_v6

def read_sibling_prefixes(filepath):
    sibling_prefixes = {}
    if os.path.exists(filepath):
        with open(filepath, "r") as fin:
            while line := fin.readline():
                line = line.strip()
                if line and line[0] != "#":
                    obj = json.loads(line)
                    prefix = obj['prefix']
                    siblings = obj['sibling_ips']
                    sibling_prefixes[prefix] = siblings
    return sibling_prefixes

def export_sibling_prefixes(sibling_prefixes, output_file):
    if len(sibling_prefixes):
        with open(output_file, "w+") as fout:
            for prefix in sibling_prefixes:
                row = {'prefix': prefix, 'sibling_ips': sibling_prefixes[prefix], 'af': '4' if '.' in prefix else '6'}
                fout.write(f"{json.dumps(row)}\n")


def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    hash_table = SiblingPrefixesHashTable()

    print("98.150.135.146 -->", hash_table.lookup("98.150.135.146"))
    print("2603:800c:4df0:84f0:d04b:131b:c731:e5c4 --> ", hash_table.lookup("2603:800c:4df0:84f0:d04b:131b:c731:e5c4"))

if (__name__  == "__main__"):
    main()
