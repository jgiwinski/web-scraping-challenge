from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo
import json

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars
collection = db.mars_collection

def scrapeIt():
    return scrape_mars.scrape()

@app.route("/")
def index():
    scraped_data = scrapeIt()
    print('hemisphere', scraped_data["mars_hemisphere"][0]["title"])
    print('hemisphere', scraped_data["mars_hemisphere"])
    return render_template("index.html", mars = scraped_data)

# @app.route("/scrape")
# def scraper(): 
#     mars = scrape_mars.scrape()
#     print('image', mars["mars_image"])
#     collection.update({}, mars, upsert=True)
#     return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

