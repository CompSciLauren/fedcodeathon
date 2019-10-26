import requests
from pprint import pprint

url = "https://trulia.p.rapidapi.com/properties/detail"

querystring = {"cy": "kansas city", "st": "KS",
               "id": "3275976158", "idt": "for rent"}

headers = {
    'x-rapidapi-host': "trulia.p.rapidapi.com",
    'x-rapidapi-key': "2af1e5f463msh56954381eaae48cp19efadjsned8106ad43f2"
}

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)
