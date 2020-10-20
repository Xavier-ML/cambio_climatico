# import necessary libraries
from flask import Flask, render_template
from flask_wtf import FlaskForm

import pymongo

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from config import usnm, pswd
from lists import series_list, country_list

# create instance of Flask app
app = Flask(__name__)

username = usnm
password = pswd
ctgrs_list = series_list
cntr_list = country_list

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.iadrt.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.climate_db

app.config['SECRET_KEY'] = 'usnmpswd'

class SearchForm(FlaskForm):
    cat_1 = StringField('Category 1', validators = [DataRequired()])
    cat_2 = StringField('Category 2', validators = [DataRequired()])
    submit = SubmitField('Search')

# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html",
    ctgrs_list = ctgrs_list,
    cntr_list = cntr_list)
    
@app.route("/Visualizations", methods = ['GET','POST'])
def visualize():
    form = SearchForm()
    return render_template("visualizations.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
