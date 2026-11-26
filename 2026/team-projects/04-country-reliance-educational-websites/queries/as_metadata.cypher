UNWIND $asns AS requested_asn
OPTIONAL MATCH (a:AS {asn: requested_asn})-[r:NAME|COUNTRY]->(n)
WHERE n:Name OR n:Country
RETURN requested_asn AS asn, type(r) AS relation, properties(r) AS relationship,
       properties(n) AS node
LIMIT $limit
