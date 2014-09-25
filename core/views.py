from flask import render_template
from .art import Art
from . import app


@app.route('/')
def index():
    return art('index')


@app.route('/<id>.html')
def art(id):
    return render_template('art.html', art=Art.load(id))
