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
engine = create_engine('sqlite:///miami.sqlite')
                    #connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
# Zip_income = Base.classes.zip_income
Restaurants = Base.classes.restaurants

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
    return render_template("templates/index.html", index=index)


@app.route("/api/v1.0/all_locations")
def locations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all restaurant names, addresses, and categories
    results = session.query(Restaurants).order_by(Restaurants.name.asc()).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/restaurants")
def restaurants():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all restaurants
    results = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .filter(Restaurants.category == 'Restaurants')\
        .order_by(Restaurants.name.asc()).all()

    session.close()
    
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/fast_food")
def fast_food():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all restaurants
    fast_food = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .filter(Restaurants.category == 'Fast Food')\
        .order_by(Restaurants.name.asc()).all()
    
    session.close()
    
    all_names = list(np.ravel(fast_food))

    return jsonify(all_names)

@app.route("/api/v1.0/supermarkets")
def supermarkets():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all restaurants
    grocery_stores = session.query(Restaurants.Name, Restaurants.Address, Restaurants.Category)\
        .filter(Restaurants.category == 'Grocery Store')\
        .order_by(Restaurants.name.asc()).all()

    session.close()

    all_names = list(np.ravel(grocery_stores))

    return jsonify(all_names)

@app.route("/api/v1.0/income_data")
def income_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query Income data in Miami zip codes
    results = session.query(Zip_income.Zipcode, Zip_income.Median_income)
    
    session.close()

    # Convert list of tuples into a normal list
    income = list(np.ravel(results))

    return jsonify(income)

if __name__ == "__main__":
    app.run(debug=True)