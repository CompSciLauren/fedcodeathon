import os

from flask import Flask, session, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route("/")
def renderIndex():
	return render_template("index.html")

@app.route("/map")
def renderMap():
	return render_template("maps-results.html")
	
if __name__ == "__main__":
	app.run()