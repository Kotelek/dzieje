from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from aplikacja import data


Articles = data.Articles()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://15_bielicz:swinki3@leszczyna.wzks.uj.edu.pl/15_bielicz'
db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)


Examples = Example.query.all()


class User(db.Model):
    __tablename__ = 'si_auth'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(80))
    fk_role_id = db.Column(db.Integer)

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Hasło', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Zapamiętaj mnie')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    login = StringField('Login', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Hasło', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html',
                           title='Home')

@app.route('/example')
def example():

    return render_template('example.html',
                           example=Examples)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/bibliography')
def bibliography():
    return render_template('bibliography.html')


@app.route('/articles')
def articles():

    return render_template('articles.html',
                           articles=Articles)


@app.route('/article/<string:id>')
def article(id):

    return render_template('article.html',
                           id=id)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(login=form.login.data, email=form.email.data, password=form.password.data, fk_role_id=2)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        print(user)

        if user:
            print(user)
            print(user.password)
            print(form.password)
            if user.password == form.password:
                print(user)
                return redirect(url_for('articles'))

        return '<h1>Invalid login or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


#app.run(host="0.0.0.0", port=5002, debug=True)

