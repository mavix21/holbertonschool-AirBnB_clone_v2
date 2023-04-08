#!/usr/bin/python3
""" This module starts a Flask Web application that listens on 0.0.0.0
    (all network interfaces) and port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Renders all states, cities, and amenities stored in the database"""
    context = {
            'states': storage.all(State).values(),
            'amenities': storage.all(Amenity).values()
            }
    return render_template("10-hbnb_filters.html", **context)


@app.teardown_appcontext
def close_session(self):
    """Removes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
