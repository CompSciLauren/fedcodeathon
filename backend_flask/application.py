import os
from data_collectors.business_scrapers import GoogleScraper, YelpScraper
from data_collectors.cost_scraper import AreaCostScraper
from data_collectors.traffic_scraper import get_traffic_lat_lng
from data_collectors.air_quality_scraper import get_quality_lat_lng
from flask import Flask, session, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route("/map")
def render_map():
    place = request.args.get('autocomplete_search')
    biz = request.args.get('business_type_search')
    rad = request.args.get('radius_search')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    return render_template("maps-results.html")

@app.route("/report")
def render_report():
    place = request.args.get('autocomplete_search')
    biz = request.args.get('business_type_search')
    rad = request.args.get('radius_search')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    area = {'lat': lat, 'lng': lng, 'radius': rad}
    g_scraper = GoogleScraper('data_collectors/google_key')
    c_scraper = AreaCostScraper('data_collectors/rent_key')
    b_list = g_scraper.get_business_list_radius(area, biz)
    c_list = c_scraper.get_cost_lat_lng(lat, lng)
    air_qual = get_quality_lat_lng(lat, lng, 'data_collectors/air_quality_key')['data']

    return render_template("report.html",
                        place=place,
                        biz=biz,
                        rad=rad,
                        biz_data=b_list['results'],
                        air_qual=air_qual,
                        cost_data=c_list)

@app.route("/map_api", methods=["GET"])
def map_api():
    biz = request.args.get('business_type_search')
    rad = request.args.get('radius_search')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    area = {'lat': lat, 'lng': lng, 'radius': rad}
    g_scraper = GoogleScraper('data_collectors/google_key')
    b_list = g_scraper.get_business_list_radius(area, biz)

    return jsonify(b_list)

@app.route("/traffic_api", methods=["GET"])
def traffic_api():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    return jsonify(get_traffic_lat_lng(lat, lng, 'data_collectors/traffic_key'))

@app.route("/air_api", methods=["GET"])
def air_api():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    return jsonify(get_quality_lat_lng(lat, lng, 'data_collectors/air_quality_key'))

@app.route("/rent_api", methods=["GET"])
def rent_api():
    place = request.args.get('autocomplete_search')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    scraper = AreaCostScraper('data_collectors/rent_key')

    return jsonify(scraper.get_cost_lat_lng(lat, lng))

    
if __name__ == "__main__":
    app.run()
