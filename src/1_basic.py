"""
Getting started;

1. pip3 install virtualenv
2. python3 -m virtualenv env (setup virual environment))
3. source env/bin/activate (source into it, 'deactivate' in terminal to exit)
4. pip3 install flask
5. pip3 freeze > requirements.txt
6. pip3 install -r requirements.txt (for future ref)
7. export FLASK_APP=1_basic.py && flask run (to start server; '&&' runs both commands)

You can also run 'export FLASK_APP={your_file.py}' to point your FLASK_APP to some file, and then you can run 'flask run'

(Make sure you're sourced into your virtualenv, this is where Flask is actually installed)
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')  # basic routing
def test():
    return 'Running!'


@app.route('/basic')  # adding another route, using inline HTML
def basic_page():
    return '<h2>Inline HTML!</h2>'


@app.route('/<parameter>')  # what you write here...
def print_name(parameter):  # ...you also write here (mismatching makes this break)
    return f'Hello, {parameter}!'


@app.route('/<non_existent>')
def test_redirect_with_param(non_existent):
    return f'Page "{non_existent}" doesn"t exist!'