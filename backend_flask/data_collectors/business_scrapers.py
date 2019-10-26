import logging as log
import googlemaps
from pprint import pprint

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
			'longitutde' : 42, # degrees
			'radius' : 1000 # meters
		}"""
		pass

class GoogleScraper(BusinessAPIScraper):
	def __init__(self, keyfile, endpoint="https://maps.googleapis.com/maps/api/place"):
		super().__init__(keyfile, endpoint)
		self.client = googlemaps.Client(self.key)

	def get_business_list_radius(self, area, b_type, language='en-US', region='US'):
		location = (area['latitude'], area['longitutde'])
		radius = area['radius']
		url = self.endpoint + '/findplacefromtext/json'
		return self.client.places(b_type, location=location, radius=radius)

if __name__ == "__main__":
	area = {
		'latitude' : 38.899090, # degrees
		'longitutde' : -94.724861, # degrees
		'radius' : 1 # miles
	}
	pprint(GoogleScraper('google_key').get_business_list_radius(area, 'restaurant'))