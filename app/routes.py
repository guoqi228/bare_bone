# need to import app varibales
from app import app
from flask import render_template  # render html files

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
