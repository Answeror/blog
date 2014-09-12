from flask import render_template
from .art import get_arts, Art
from . import app


@app.route('/')
def index():
    return render_template('index.html', arts=get_arts())


@app.route('/<id>.html')
def art(id):
    return render_template('art.html', art=Art.load(id))
