# Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2

from flask import Flask, render_template, jsonify, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

#################################################
# Database Setup
#################################################

# Create engine
engine = create_engine('postgresql://postrgres:postgres@localhost:5432/miami')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
#?????

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postres:postres@localhost:5432/miami'

db=SQLAlchemy(app)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()