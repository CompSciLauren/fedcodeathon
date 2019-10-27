import requests

headers = {"Basic": "kelyn@crandall.me:t1Y@epnU^AuBiaNs7PFX"}
url = 'https://sandbox-rest.avatax.com/api/v2/taxrates/byaddress'

class TaxScraper:
	def __init__(self):
		querystring = {'line1': '12600 S Quivira Rd', 'city': 'Overland Park', 'country': 'US', 'region': 'KS', 'postalCode': '66213'}
		req = requests.request("GET", url, headers=headers, params=querystring)
		print(req)

if __name__ == "__main__":
	TaxScraper()