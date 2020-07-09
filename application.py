from flask import Flask, render_template
from wtforms_fields import *
from models import *

app = Flask(__name__)
app.secret_key = "replace later"

# Configure Database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qpwncruxgggjbf:1f1a3fbfcdfc9fe4f533e2df28498cbae5c9a1e7f1fb9e771cc14efda1c2fbee@ec2-3-216-129-140.compute-1.amazonaws.com:5432/das9c4gpm5n13l'

db.init_app(app)

@app.route('/', methods = ['GET','POST'])

def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        #Check username exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username!"

        # Add user to DB  

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"

    return render_template('index.html', form = reg_form)

if __name__ == "__main__":
    app.run(debug=True)