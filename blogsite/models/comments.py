from time import timezone
from datetime import datetime
from sqlalchemy import true
from db import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# user model


class CommentModel(db.Model):
	__tablename__ = "comments"
	id = db.Column(db.Integer(), primary_key=True)
	text = db.Column(db.Text(3000), nullable=False, unique=False)
	author = db.Column(db.Text, db.ForeignKey('user.username', ondelete="CASCADE"), nullable=False)
	date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
	article_id = db.Column(db.Integer, db.ForeignKey(
    'article.id', ondelete="CASCADE"), nullable=False)

