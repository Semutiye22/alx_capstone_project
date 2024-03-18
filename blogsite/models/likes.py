from time import timezone
from datetime import datetime
from sqlalchemy import true
from db import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# user model


class LikeModel(db.Model):
	__tablename__ = "likes"
	id = db.Column(db.Integer(), primary_key=True)
	author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
	date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
	article_id = db.Column(db.Integer, db.ForeignKey(
            'article.id', ondelete="CASCADE"), nullable=False)
