#!/usr/bin/python3
""" Module is for a minimal Flask web application. """
from flask import Flask, render_template
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


@app.route('/number/<int:num>')
def number_route(num):
    """ Number route for Flask web app. Same as C, but with data validation """
    return '{} is a number'.format(escape(num))


@app.route('/number_template/<int:num>')
def number_template_route(num):
    """ Number route 2 for Flask web app. Same as Number, but Jinga2 html """
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>')
def number_odd_or_even_route(num):
    """ Odd/Even route for Flask web app. Same as Num 2 with odd/even check """
    return render_template('6-number_odd_or_even.html', num=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0')