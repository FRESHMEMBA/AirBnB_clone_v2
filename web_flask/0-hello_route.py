#!/usr/bin/python3

"""
Starts a Flask web application:

Web application listens on 0.0.0.0, port 5000
Routes:
/airbnb-onepage/: display “Hello HBNB!”
Uses the option strict_slashes=False in route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
