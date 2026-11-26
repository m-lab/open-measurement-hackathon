UNWIND $ips AS requested_ip
OPTIONAL MATCH (i:IP {ip: requested_ip})-[m:PART_OF]->(p:BGPPrefix)
OPTIONAL MATCH (p)<-[r:ORIGINATE]-(a:AS)
RETURN requested_ip AS ip, p.prefix AS prefix, properties(m) AS membership,
       a.asn AS asn, properties(r) AS relationship
LIMIT $limit
