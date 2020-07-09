from ext import *

db = SQLAlchemy()

class User(db.Model):
    """ User Model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

    db.create_all()