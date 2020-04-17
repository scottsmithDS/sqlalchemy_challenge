import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


Measurement= Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.prcp , Measurement.date).all()
    session.close()
    Measurements = list(np.ravel(results))
    return jsonify(Measurements)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station).all()
    session.close()
    Stations = list(np.ravel(results))
    return jsonify(Stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.tobs).all()
    session.close()
    Tobs = list(np.ravel(results))
    return jsonify(Tobs)

@app.route("/api/v1.0/<start>")
def start():
    session = Session(engine)
    results = session.query(Measurement.date).all()
    session.close()
    MDate = list(np.ravel(results))
    return jsonify(MDate)

@app.route("/api/v1.0/<start>/<end>")
def end():
    session = Session(engine)
    results = session.query(Measurement.date).all()
    session.close()
    MDateE = list(np.ravel(results))
    return jsonify(MDateE)

if __name__ == '__main__':
    app.run(debug=True)
