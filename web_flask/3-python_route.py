#!/usr/bin/python3

"""
Starts a Flask web application:

Web application listens on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display "HBNB"
/c/<text>: display "C" followed by the value of the text variable
/python/<text>: display "Python" followed by the value of the text variable
    The default value of text is "is cool"
Uses the option strict_slashes=False in route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return f"Python {text.replace('_', ' ')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
