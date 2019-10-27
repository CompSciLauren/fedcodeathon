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
    'x-rapidapi-key': 'hidden'
}


class AreaCostScraper:
    def __init__(self, keyfile):
        headers['x-rapidapi-key'] = open(keyfile, "r").read().strip()

    def get_cost_address(self, address):
        querystring = {"address": address}

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        results = response.json()

        return results

    def get_cost_lat_lng(self, lat, lng):
        querystring = {'longitude': lng, 'latitude': lat}

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        results = response.json()

        return results

if __name__ == "__main__":
    #pprint(AreaCostScraper('rent_key').get_cost_address("7603 Monrovia St, Lenexa, KS"))
    pprint(AreaCostScraper('rent_key').get_cost_lat_lng(38.899090, -94.724861))
"""
rjstuff = response.json()
results = rjstuff['result']

pprint(results)

for result in rjstuff['result']:
    print(result['id'])
"""
