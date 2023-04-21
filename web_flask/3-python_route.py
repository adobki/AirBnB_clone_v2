#!/usr/bin/python3
""" Module is for a minimal Flask web application. """
from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Hello world function and homepage for Flask web app """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """ hbnb route for Flask web app """
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """ c route for Flask web app. Outputs given text without underscores """
    return 'C {}'.format(escape(text)).replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python_route(text='is cool'):
    """ Python route for Flask web app. Same as C, but with default text """
    return 'Python {}'.format(escape(text)).replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
