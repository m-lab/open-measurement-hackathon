UNWIND $hosts AS requested_host
OPTIONAL MATCH (h:HostName {name: requested_host})
OPTIONAL MATCH (h)-[r:RESOLVES_TO|ALIAS_OF|PART_OF]->(n)
WHERE n:IP OR n:HostName OR n:DomainName
RETURN requested_host AS host, h IS NOT NULL AS exists,
       type(r) AS relation, properties(r) AS relationship,
       labels(n) AS node_labels, properties(n) AS node
LIMIT $limit
