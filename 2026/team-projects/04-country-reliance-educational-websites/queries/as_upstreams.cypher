UNWIND $asns AS requested_asn
OPTIONAL MATCH (a:AS {asn: requested_asn})<-[r:PEERS_WITH]-(u:AS)
WHERE (r.reference_name IN ['caida.as_relationships_v4','caida.as_relationships_v6'] AND r.rel = -1)
   OR (r.reference_name = 'bgpkit.as2rel' AND r.rel = 1)
RETURN requested_asn AS asn, u.asn AS upstream_asn, properties(r) AS relationship
LIMIT $limit
