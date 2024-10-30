# Import the dependencies.
# Import necessary libraries
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
import numpy as np



#################################################
# Database Setup
#################################################

# Create engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)



# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)



# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():

    return (f"Welcome to Hawaii Analysis<br/>"
            f"available routes<br/>"
             f"/api/v1.0/precipitation<br/>"
              f"/api/v1.0/stations<br/>"
               f"/api/v1.0/tobs<br/>"
                f"/api/v1.0/<start><br/>"
                 f"/api/v1.0/<start>/<end><br/>" )

@app.route("/api/v1.0/precipitation")
def percipitation():
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    percipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_ago).all()
    
    session.close()
    percipitationdic={date:prcp for date, prcp in percipitation_data}


    return jsonify(percipitationdic)

if __name__ == '__main__':
    app.run()