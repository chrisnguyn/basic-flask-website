"""
Getting started;

1. pip3 install virtualenv
2. python3 -m virtualenv env
3. source env/bin/activate
4. pip3 install flask
5. pip freeze > requirements.txt
6. pip install -r requirements.txt (for future ref)
7. export FLASK_APP=basic.py && flask run (to start server)
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')  # basic routing
def test():
    return 'Running!'


@app.route('/basic')  # adding another route
def basic_page():
    return '<h2>Inline HTML!</h2>'


@app.route('/<parameter>')  # what you write here...
def print_name(parameter):  # you also write here
    return f'Hello, {parameter}!'