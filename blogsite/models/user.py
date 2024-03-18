from time import timezone
from datetime import datetime
from sqlalchemy import true
from db import db
from flask_login import UserMixin
from sqlalchemy.sql import func


#user model
class UserModel(db.Model, UserMixin):
	__tablename__ = "user"
	id =  db.Column(db.Integer(), primary_key = True) 
	firstname = db.Column(db.String(255), nullable = False, unique = False)
	lastname = db.Column(db.String(255), nullable=False, unique=False)
	username = db.Column(db.String(255), nullable = False, unique = False)
	email = db.Column(db.String(255), nullable = False, unique = True)
	password_hash = db.Column(db.String())
	date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
	articles = db.relationship('ArticleModel', backref='user', passive_deletes=True)