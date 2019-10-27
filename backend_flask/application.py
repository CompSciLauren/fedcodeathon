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
	return render_template("maps-results.html")

@app.route("/report")
def render_report():
	place = request.args.get('autocomplete_search')
	biz = request.args.get('business_type_search')
	rad = request.args.get('radius_search')
	g_scraper = GoogleScraper()
	b_list = g_scraper.get_business_list_radius()
	return render_template("")
	
if __name__ == "__main__":
	app.run()
