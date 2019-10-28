from pprint import pprint
import json
import requests
from pprint import pprint


def get_traffic_lat_lng(lat, lng, keyfile):
    api_key = open(keyfile).read().strip()
    url = 'http://api.walkscore.com/score'
    querystring = {'format': 'json',
                    'lat': str(lat),
                    'lon': str(lng),
                    'transit': '1',
                    'bike': '1',
                    'wsapikey': api_key}
    response = requests.get(url, params=querystring)

    results = response.json()
    print(results)

    results.setdefault('transit', {'description': None, 'score': None, 'summary': None})
    results.setdefault('bike', {'description': None, 'score': None, 'summary': None})

    return results

if __name__ == "__main__":
    pprint(get_traffic_lat_lng(38.899090, -94.724861, 'traffic_key'))