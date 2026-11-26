UNWIND $countries AS requested_country
MATCH (c:Country {country_code: requested_country})<-[cr:COUNTRY]-(ranking:Ranking)<-[r:RANK]-(a:AS)
WHERE r.reference_name = 'ihr.country_dependency' AND r.rank <= 10
RETURN requested_country AS country_code, ranking.name AS ranking,
       a.asn AS asn, properties(r) AS relationship, properties(cr) AS country_relationship
LIMIT $limit
