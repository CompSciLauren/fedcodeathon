from pprint import pprint
import json
import requests


class TrafficScraper:
    def get_traffic(self, lat, lang, api_key):
        url = 'http://api.walkscore.com/score?format=json&lat=' + lat + \
            '&lon=' + lang + '&transit=1&bike=1&wsapikey=' + api_key
        response = requests.request("GET", url)

        results = response.json()

        return results
