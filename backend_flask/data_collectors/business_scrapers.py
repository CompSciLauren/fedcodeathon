import logging as log
import googlemaps
from pprint import pprint
import requests
import json

class BusinessAPIScraper:
    def __init__(self, keyfile, endpoint):
        self.keyfile = keyfile
        self.endpoint = endpoint
        self.key = open(keyfile, "r").read().strip()

    def get_business_list_radius(self, area, b_type):
        """
        Return a list of businesses of given type in given area
        area = {
            'latitude' : 37.5, # degrees
            'longitude' : 42, # degrees
            'radius' : 1000 # meters
        }"""
        pass

class GoogleScraper(BusinessAPIScraper):
    def __init__(self, keyfile, endpoint="https://maps.googleapis.com/maps/api/place"):
        super().__init__(keyfile, endpoint)
        self.client = googlemaps.Client(self.key)

    def get_business_list_radius(self, area, b_type, language='en-US', region='US'):
        location = (area['latitude'], area['longitude'])
        radius = area['radius']
        url = self.endpoint + '/findplacefromtext/json'
        return self.client.places(b_type, location=location, radius=radius)

class YelpScraper(BusinessAPIScraper):
    def __init__(self, keyfile, endpoint="https://api.yelp.com/v3/businesses"):
        super().__init__(keyfile, endpoint)

    def get_business_list_radius(self, area, b_type):
        headers = {'Authorization': 'Bearer %s' % self.key}
        # In the dictionary, term can take values like food, cafes or businesses like McDonalds
        # params = {'term': 'seafood', 'location': 'New York City'}
        params = {'term': b_type, 'longitude': area['longitude'], 'latitude': area['latitude']}

        # Making a get request to the API
        req = requests.get(self.endpoint+'/search', params=params, headers=headers)

        # proceed only if the status code is 200
        if req.status_code != 200:
            log.warning('The Yelp API status is {}'.format(req.status_code))

        # printing the text from response
        return json.loads(req.text)


if __name__ == "__main__":
    area = {
        'latitude' : 38.899090, # degrees
        'longitude' : -94.724861, # degrees
        'radius' : 1 # miles
    }
    #google
    pprint(GoogleScraper('google_key').get_business_list_radius(area, 'restaurant'))

    #yelp
    pprint(YelpScraper('yelp_key').get_business_list_radius(area, "restaurant"))
