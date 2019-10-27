import os
from data_collectors.business_scrapers import GoogleScraper, YelpScraper
from flask import Flask, session, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def render_index():
	return render_template("index.html")

@app.route("/map")
def render_map():
	place = request.args.get('autocomplete_search')
	print(place)
	biz = request.args.get('business_type_search')
	print(biz)
	rad = request.args.get('radius_search')
	print(rad)
	lat = request.args.get('lat')
	print(lat)
	lng = request.args.get('lng')
	print(lng)
	return render_template("maps-results.html")

@app.route("/report")
def render_report():
	place = request.args.get('autocomplete_search')
	biz = request.args.get('business_type_search')
	rad = request.args.get('radius_search')
	lat = request.args.get('lat')
	lng = request.args.get('lng')
	g_scraper = GoogleScraper('data_collectors/google_key')
	area = {'lat': lat, 'lng': lng, 'radius': rad}
	b_list = g_scraper.get_business_list_radius(area, biz)
	output = 'hi'
	return render_template("report.html", output=output)
	
if __name__ == "__main__":
	app.run()
