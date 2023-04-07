#!/usr/bin/python3
""" This module starts a Flask Web application that listens on 0.0.0.0
    (all network interfaces) and port 5000
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_webapp():
    """Returns the message we want to display in the user's browser"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Returns the message we want to display in the user's browser"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    """Returns the message we want to display in the user's browser"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
