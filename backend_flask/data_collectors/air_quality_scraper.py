import requests
import json
from pprint import pprint

def get_quality_by_lat_lng(lat, lng, keyfile):
    api_key = open(keyfile).read().strip()
    url = 'https://api.breezometer.com/air-quality/v2/current-conditions'
    querystring = {'lat': lat,
                    'lon': lng,
                    'key': api_key
    }
    response = requests.get(url, params=querystring)

    results = response.json()

    return results

if __name__ == "__main__":
    print(get_quality_by_lat_lng(38.899090, -94.724861, 'air_quality_key'))