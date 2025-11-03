Here's my query

query = '''
SELECT a.TestTime,
raw.ClientIP,
client.Geo.Latitude as client_latitude,
client.Geo.Longitude as client_long,
client.Geo.City AS client_city,
client.Geo.PostalCode AS client_postal,
client.Geo.CountryCode AS client_country,
client.Network.ASNumber,
client.Network.ASName,
raw.ServerIP,
server.Site,
server.Machine,
server.Geo.Latitude as server_latitude,
server.Geo.Longitude as server_longitude,
server.Geo.City AS server_city,
server.Geo.CountryCode AS server_country,
a.LossRate,
a.MinRTT,
a.MeanThroughputMbps
FROM `measurement-lab.ndt.ndt7`
WHERE date <= "2025-10-30" AND date >= "2025-01-01"
AND client.Geo.CountryCode = "NZ"
'''
df = pd.read_gbq(query, project_id="measurement-lab")
