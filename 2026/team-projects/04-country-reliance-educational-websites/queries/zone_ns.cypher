UNWIND $zones AS requested_zone
OPTIONAL MATCH (d:DomainName {name: requested_zone})-[r:MANAGED_BY]->(n:AuthoritativeNameServer)
RETURN requested_zone AS zone, n.name AS name, properties(r) AS relationship
LIMIT $limit
