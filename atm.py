

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atm.db' 

db = SQLAlchemy(app)



class Account(db.Model):
	id = db.Column(db.Integer, primary_key =True)
	account_number = db.Column(db.Integer, unique=True, nullable=False)
	pin = db.Column(db.Integer, unique=False, nullable=False)
	balance = db.Column(db.Integer)
	names = db.Column(db.Text)
	
