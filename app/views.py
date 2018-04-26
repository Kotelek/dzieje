from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html',
                           title='Home')


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/signup')
def signup():
    return render_template('events.html')


@app.route('/login')
def login():
    return render_template('events.html')