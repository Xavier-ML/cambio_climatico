# import necessary libraries
from flask import Flask, render_template

import config
import lists

# create instance of Flask app
app = Flask(__name__)

username = usnm
password = pswd
ctgrs_list = series_list
cntr_list = country_list

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.iadrt.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.climate_db

# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html",
    ctgrs_list = ctgrs_list,
    cntr_list = cntr_list)
    
@app.route("/visualizations")
def visualize():
    return render_template("visualizations.html")


if __name__ == "__main__":
    app.run(debug=True)
