"""
Rendering a .html file inside of Flask.
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_page():
    return render_template('3_html_templates.html')  # file must be inside a folder called 'templates' which is in the same directory as the .py file currently
