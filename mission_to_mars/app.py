from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo
import json

app = Flask(__name__)

collection = {}

# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# db = client.mars
# collection = db.mars_collection

@app.route("/")
def index():
    return render_template("index.html", mars = collection, empty = len(collection))

@app.route("/scrape")
def scraper(): 
    global collection
    collection = scrape_mars.scrape()
    
    # collection.update({}, mars, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

