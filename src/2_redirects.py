"""
Testing page redirects. For example, if a user navigates to some undefined page, reroute them back to the main page.

'export FLASK_APP=2_redirects.py && flask run'
"""

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def test():
    return 'Welcome to the main page!'


@app.route('/<anything>')
def doesntexist(anything):
    return redirect(url_for('test'))  # reroute user to 'test' function (write function name here, not path)
