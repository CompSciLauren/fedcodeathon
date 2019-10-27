import requests
import json
from pprint import pprint


class AirQualityScraper:
    def get_quality_by_latLong(self, lat, long, api_key):
        url = 'https://api.breezometer.com/air-quality/v2/current-conditions?lat=' + lat + \
            '&lon=' + long + '&key=' + api_key
        response = requests.request("GET", url)

        results = response.json()

        return results
