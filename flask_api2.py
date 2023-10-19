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
engine = create_engine("sqlite:///locations.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
locations = Base.classes.locations
income = Base.classes.income

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    return render_template("index.html", index=index)

@app.route("/api/v1.0/restaurants")
def restaurants():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(locations.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    @app.route("/api/v1.0/fast_food")
def fast_food():
# Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(locations.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

    @app.route("/api/v1.0/supermarkets")
def supermarkets():
    # Create our session (link) from Python to the DB
    session = Session(engine1)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(locations1.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/income")
def income():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(income.name).all()

    result = session.query(User, Document).select_from(join(User, Document)).filter(User.email=='user@email.com').all()

    # Find the most active station
    most_active_stations = session.query(
        income.station, func.count(income.station)
    ).group_by(income.station)
    most_active_stations = most_active_stations.order_by(
        func.count(income.station).desc()
    ).all()
    most_active_station = most_active_stations[0][0]

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


if __name__ == "__main__":
    app.run(debug=True)
