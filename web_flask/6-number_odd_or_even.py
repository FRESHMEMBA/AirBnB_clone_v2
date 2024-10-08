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
/number/<n>: display "n is a number" only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
    H1 tag: "Number: n" inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer
    H! tag: "Number: n is even|odd" inside the tag BODY
Uses the option strict_slashes=False in route definition
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    evenness = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
