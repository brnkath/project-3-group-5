# Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify, redirect, url_for


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///miami.sqlite",
                       connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Zip_income = Base.classes.zip_income
Restaurants = Base.classes.restauants

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Can the routes have spaces?
@app.route("/")
def index():
    """List all available api routes."""
    return( 
        f"Available Routes:<br/>" 
        f"/api/v1.0/All Locations<br/>" 
        f"/api/v1.0/Locations By Category<br/>"
        f"/api/v1.0/Income Data<br/>"
    return render_template("index.html", index=index))


@app.route("/api/v1.0/All Locations")
def locations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all restaurant names, addresses, and categories
    results = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .order_by(Restaurants.name.asc()).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/Locations By Category<br/>")
def location_category():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all restaurants
    restaurants = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .filter(Restaurants.category == 'Restaurants')\
        .order_by(Restaurants.name.asc()).all()

    fast_food = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .filter(Restaurants.category == 'Fast Food')\
        .order_by(Restaurants.name.asc()).all()

    grocery_stores = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .filter(Restaurants.category == 'Grocery Store')\
        .order_by(Restaurants.name.asc()).all()

    session.close()

    # Select cetegory


    # Return the data from the appropriate category
    if RESTAURANT:
        return jsonify(restaurants)
    
    if FASTFOOD:
        return jsonify(fast_food)
    
    if GROCERY:
        return jsonify(grocery_stores)

@app.route("/api/v1.0/Income Data<br/>")
def zip_income():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Income data in Miami zip codes
    results = session.query(Zip_income.Zipcode, Zip_income.Median_income)
    
    session.close()

    # Convert list of tuples into normal list
    income = list(np.ravel(results))

    return jsonify(income)

if __name__ == "__main__":
    app.run(debug=True)
