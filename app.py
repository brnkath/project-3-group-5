# Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func
import psycopg2

from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################

engine = create_engine('postgresql://postgres:postgres@localhost:5432/miami')
metadata = MetaData()
metadata.reflect(bind=engine)

Base = automap_base(metadata=metadata)
Base.prepare()

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postres:postres@localhost:5432/miami'

# miami=SQLAlchemy(app)

# class Zip_income(miami.Model):
#     __tablename__='zip_income'
#     id=miami.Column(miami.Integer, primary_key=True)
#     zipcode=miami.Column(miami.String())
#     median_income=miami.Column(miami.Float())

# def __init__(self, zipcode, median_income):
#     self.zipcode = zipcode
#     self.median_income = median_income

# class Restaurants(miami.Model):
#     __tablename__='restaurants'
#     id=miami.Column(miami.Integer, primary_key=True)
#     name=miami.Column(miami.String())
#     address=miami.Column(miami.String())
#     category=miami.Column(miami.String())

# def __init__(self, name, address, category):
#     self.name = name
#     self.address = address
#     self.category = category

Restaurants = Base.classes.restaurants
Zip_income = Base.classes.zip_income

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1.0/all_locations", methods=['GET'])
def get_locations():
    
    session = Session(engine)
    
    if request.method == 'GET':
        locations = db.session.query(Restaurants).order_by(Restaurants.name.asc()).all()
    
    # return locations
    all_names = [dict(name=row.name, address=row.address, category=row.category) for row in locations]
    
    session.close()
    
    return jsonify(all_names)


@app.route("/api/v1.0/restaurants", methods=['GET'])
def get_restaurants():
    
    session = Session(engine)
    
    # Query all restaurants     
    if request.method == 'GET':
        results = db.session.query(Restaurants.name, Restaurants.address, Restaurants.category)\
            .filter(Restaurants.category == 'Restaurants')\
            .order_by(Restaurants.name.asc()).all()
 
     # results = list(np.ravel(results))   
 
    session.close()
    
    return jsonify(results)    


@app.route("/api/v1.0/fast_food", methods=['GET'])
def get_fast_food():
    
    session = Session(engine)
    
    # Query all fast food restaurants    
    if request.method =='GET':
        fast_food = db.session.query(Restaurants.name, Restaurants.address, Restaurants.category)\
            .filter(Restaurants.category == 'Fast Food')\
            .order_by(Restaurants.name.asc()).all()
        
     # fast_food = list(np.ravel(fast_food))   
 
    session.close()
    
    return jsonify(fast_food)  

@app.route("/api/v1.0/supermarkets", methods=['GET'])
def get_supermarkets():
    
    session = Session(engine)
    
    # Query all supermarkets
    if request.method =='GET':
        results = db.session.query(Restaurants.name, Restaurants.address, Restaurants.category)\
            .filter(Restaurants.category == 'Grocery Store')\
            .order_by(Restaurants.name.asc()).all()        

     # results = list(np.ravel(results))   
 
    session.close()
    
    return jsonify(results)  


@app.route("/api/v1.0/income_data", methods=['GET'])
def get_income_data():
    
    session = Session(engine)
    
    if request.method == 'GET':
        results = db.session.query(Zip_income.zipcode, Zip_income.median_income).all()

     # results = list(np.ravel(results))   
 
    session.close()
    
    return jsonify(results)  

if __name__ == '__main__':
   app.run(debug=True)