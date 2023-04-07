#!/usr/bin/python3
""" This module starts a Flask Web application that listens on 0.0.0.0
    (all network interfaces) and port 5000
"""
from flask import Flask, redirect, render_template
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
def hello_c(text):
    """Returns the message we want to display in the user's browser"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python/", strict_slashes=False)
def python_is_cool():
    """Returns the message we want to display in the user's browser"""
    return redirect("/python/is_cool")


@app.route("/python/<text>", strict_slashes=False)
def hello_python(text):
    """Returns the message we want to display in the user's browser"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def only_if_number(n):
    """Returns only if n is a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display the int in a h1 tag"""
    return (render_template('5-number.html', num=escape(n)))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_parity(n):
    return (render_template("6-number_odd_or_even.html", num=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
