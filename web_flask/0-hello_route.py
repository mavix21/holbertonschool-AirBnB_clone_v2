#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_webapp():
    return "Hello HBNB!"


if __name__ == "__main__":
    """
    Run the Flask application on 0.0.0.0 (all network interfaces) and port 500
    """
    app.run(host="0.0.0.0", port=5000)
