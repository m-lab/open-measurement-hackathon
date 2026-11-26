UNWIND $ips AS requested_ip
OPTIONAL MATCH (i:IP {ip: requested_ip})-[m:PART_OF]->(p:GeoPrefix)
OPTIONAL MATCH (p)-[r:COUNTRY]->(c:Country)
RETURN requested_ip AS ip, p.prefix AS prefix, properties(m) AS membership,
       c.country_code AS country_code, properties(r) AS relationship
LIMIT $limit
