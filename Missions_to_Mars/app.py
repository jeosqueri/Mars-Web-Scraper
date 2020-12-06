from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict=mars_dict)

#This is what can create the scrape button for HW
@app.route("/scrape")
def scraper():
    mars_dict = mongo.db.mars_dict  #Creates collection
    mars_data = scrape_mars.scrape()   #Calls scrape_craiglist function
    mars_dict.update({}, mars_data, upsert=True)  #Upsert will update DB
    return redirect("/", code=302)  #Return user to homepage after scrape is done


if __name__ == "__main__":
    app.run(debug=True)