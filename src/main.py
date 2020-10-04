"""
Getting started;

1. pip3 install virtualenv
2. python3 -m virtualenv env
3. source env/bin/activate
4. pip3 install flask
5. pip freeze > requirements.txt
6. pip install -r requirements.txt (for future ref)
7. export FLASK_APP=main.py && flask run (to start server)
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'Running!'


@app.route('/hello')
def hello_world():
    return 'Hello, world!'


@app.route('/basic')
def basic_page():
    return '<h2>Inline HTML!</h2>'