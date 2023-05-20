#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
   /hbnb: Displays 'HBNB'
  /c/<text>: display 'C' followed by the symbol
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns 'HBNB'"""
    return 'HBNB'


@app.route('/c/<path:text>')
def display_c(text):
    """Returns C followed by text"""
    sub_path = ""
    for sub in text:
        if sub == "_":
            sub_path += " "
        sub_path += sub
    return "C {}".format(escape(sub_path))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
