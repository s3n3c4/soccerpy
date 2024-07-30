import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "f033ca41590a3b68683b491857e83925"
    }

conn.request("GET", "/teams/statistics?season=2024&team=127&league=73", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
