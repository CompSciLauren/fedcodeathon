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

url = "https://realtymole-rental-estimate-v1.p.rapidapi.com/rentalPrice"
headers = {
    'x-rapidapi-host': "realtymole-rental-estimate-v1.p.rapidapi.com",
    'x-rapidapi-key': "hidden"
}


class AreaCostScraper():
    def get_area_cost(self, address):
        querystring = {"address": address}

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        results = response.json()

        return results


#pprint(AreaCostScraper().get_area_cost("7603 Monrovia St, Lenexa, KS"))

"""
rjstuff = response.json()
results = rjstuff['result']

pprint(results)

for result in rjstuff['result']:
    print(result['id'])
"""
