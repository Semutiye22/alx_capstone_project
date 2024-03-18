from time import timezone
from datetime import datetime
from sqlalchemy import true
from db import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class ArticleModel(db.Model):
	__tablename__ = "article"
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(550))
	bodytext = db.Column(db.Text(3000), nullable=False, unique=False)
	author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
	date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
	comments = db.relationship('CommentModel', backref='article', lazy=True)


