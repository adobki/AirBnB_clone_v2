#!/usr/bin/python3
""" Module is for a minimal Flask web application. """
from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
