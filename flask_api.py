# Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify, request, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy

#################################################
# Database Setup
#################################################
#engine = create_engine('sqlite:///miami.sqlite')
                    #connect_args={'check_same_thread': False})

engine = create_engine('postgresql://postrgres:postgres@localhost/miami')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
# Zip_income = Base.classes.zip_income
#Restaurants = Base.classes.restaurants

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

db=sqlalchemy(app)

class Zip_income(db.Model):
    __tablename__='zip_income'
    id=db.Column(db.Integer, primary_key=True)
    Zipcode=db.Column(db.String())
    Median_income=db.Column(db.Double())

def __init__(self, Zipcode, Median_income):
    self.Zipcode = Zipcode
    self.Median_income = Median_income

class Restaurants(db.Model):
    __tablename__='restaurants'
    id=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String())
    Address=db.Column(db.String())
    Category=db.Column(db.String())

def __init__(self, Name, Address, Category):
    self.Name = Name
    self.Address = Address
    self.Category = Category

# Can the routes have spaces?
@app.route("/")
def index():
    return render_template("templates/index.html", index=index)

@app.route("/api/v1.0/all_locations", methods=['GET'])
def locations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    if request.method == 'GET':
        locations = db.session.query(Restaurants).order_by(Restaurants.name.asc())


    """Return a list of all passenger names"""
    # Query all restaurant names, addresses, and categories
    # results = session.query(Restaurants).order_by(Restaurants.name.asc()).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(locations))

    return jsonify(all_names)


@app.route("/api/v1.0/restaurants", methods=['GET'])
def restaurants():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)  
     
    if request.method == 'GET':
        results = db.session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
            .filter(Restaurants.category == 'Restaurants')\
            .order_by(Restaurants.name.asc()).all()


    # Query all restaurants


    session.close()
    
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/fast_food", methods=['GET'])
def fast_food():
    # Create our session (link) from Python to the DB
    session = Session(engine)    
    
    if request.method =='GET':
        fast_food = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
            .filter(Restaurants.category == 'Fast Food')\
            .order_by(Restaurants.name.asc()).all()
        


    # Query all restaurants

    session.close()
    
    all_names = list(np.ravel(fast_food))

    return jsonify(all_names)

@app.route("/api/v1.0/supermarkets", methods=['GET'])
def supermarkets():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    if request.method =='GET':
        grocery_stores = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
            .filter(Restaurants.category == 'Grocery Store')\
            .order_by(Restaurants.name.asc()).all()        


    # Query all restaurants


    session.close()

    all_names = list(np.ravel(grocery_stores))

    return jsonify(all_names)

@app.route("/api/v1.0/income_data", methods=['GET'])
def income_data():

    # Create our session (link) from Python to the DB
    session = Session(engine) 
       
    if request.method =='Get':
        results = session.query(Zip_income.Zipcode, Zip_income.Median_income)



    # Query Income data in Miami zip codes
    
    
    #session.close()

    # Convert list of tuples into a normal list
    income = list(np.ravel(results))

    return jsonify(income)

if __name__ == "__main__":
    app.run(debug=True)