UNWIND $ips AS requested_ip
OPTIONAL MATCH (i:IP {ip: requested_ip})-[m:PART_OF]->(p:BGPPrefix)
OPTIONAL MATCH (p)-[r:CATEGORIZED]->(t:Tag)
WHERE t.label = 'Anycast'
RETURN requested_ip AS ip, p.prefix AS prefix, properties(m) AS membership,
       t.label AS tag, properties(r) AS relationship
LIMIT $limit
