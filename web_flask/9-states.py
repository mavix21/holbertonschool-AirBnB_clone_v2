#!/usr/bin/python3
""" This module starts a Flask Web application that listens on 0.0.0.0
    (all network interfaces) and port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def render_states_list():
    """Renders all states stored in the database"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def render_state_by_id(id):
    """Renders all states stored in the database"""
    state = None
    states = storage.all(State)
    if id in [state.id for state in states.values()]:
        state = states.get(f'State.{id}')

    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_session(self):
    """Removes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
