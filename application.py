from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from wtforms_fields import *
from ext import db
from passlib.hash import pbkdf2_sha256
from models import *

app = Flask(__name__)
app.secret_key = "replace later"

# Configure Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ahbmnnncaxrzkb:72ddac88de0c7dbf0520676340215e4977f06e8505a0b78265a307afd22fd030@ec2-34-233-226-84.compute-1.amazonaws.com:5432/dfjoh3pdfha3dm'

db.init_app(app)

#Configure Flask login

login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/', methods = ['GET','POST'])

def index():

    reg_form = RegistrationForm()

    #Updated database if validation success

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        #Hash of the password

        hashed_pswd = pbkdf2_sha256.hash(password)

        # Add user to DB  

        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()
        flash('Registered Account Succesfully! :)... Please Log in.','success')


        return redirect(url_for('login'))

    return render_template('index.html', form = reg_form)

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()

    #Allow login if validation success

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))
        

    return render_template("login.html", form=login_form)

@app.route('/chat', methods =['GET','POST'])

def chat():
    if not current_user.is_authenticated:
        flash('Please log in.','danger')
        return redirect(url_for('login'))
    return "Chat with me!"

@app.route('/logout', methods =['GET','POST'])

def logout():
    logout_user()
    flash('You have logged out succesfully','success')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)