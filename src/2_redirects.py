"""
Testing page redirects.

export FLASK_APP=2_redirects.py && flask run
"""

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def test():
    return 'Welcome to the main page!'


@app.route('/<anything>')
def doesntexist(anything):
    return redirect(url_for('test'))  # reroute user to 'test' function
