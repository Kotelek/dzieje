from flask import render_template
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://15_bielicz:haselko@leszczyna.wzks.uj.edu.pl/15_bielicz'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('Hasło', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Zapamiętaj mnie')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Login', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('Hasło', validators=[InputRequired(), Length(min=8, max=80)])

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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


if __name__ == '__main__':
   app.run(debug=True)