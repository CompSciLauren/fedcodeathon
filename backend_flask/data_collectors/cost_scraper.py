import requests
import json
from pprint import pprint

"""
url = "https://trulia.p.rapidapi.com/locations/auto-complete"

querystring = {"srch": "kansas city", "idt": "for rent"}

headers = {
    'x-rapidapi-host': "trulia.p.rapidapi.com",
    'x-rapidapi-key': "2af1e5f463msh56954381eaae48cp19efadjsned8106ad43f2"
}

response = requests.request("GET", url, headers=headers, params=querystring)
rjstuff = response.json()

results = rjstuff['result']

pprint(results)

for result in rjstuff['result']:
    print(result['id'])
"""

headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'Provided access token'
}
response = requests.request("GET",
                            'http://api.walkscore.com/score?format=json&lat=39.123986709552&lon=-94.55402165065&transit=1&bike=1&wsapikey=37549c9690a7077d47447248f074dc15')

pprint(response.text)


#pprint(AreaCostScraper().get_area_cost("7603 Monrovia St, Lenexa, KS"))

"""
rjstuff = response.json()
results = rjstuff['result']

pprint(results)

for result in rjstuff['result']:
    print(result['id'])
"""
