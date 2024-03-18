from flask import Flask
from flask_login import LoginManager, login_manager
from blogsite.models import UserModel, ArticleModel, CommentModel, LikeModel
from db import db
import os
from blogsite.resources.user import auth as UserBlueprint
from blogsite.resources.article import article as ArticleBlueprint
from blogsite.resources.aven import aven as AvenBlueprint



DB_NAME = 'blog2.db'

# generate current path
base_dir = os.path.dirname(os.path.realpath(__file__))


def create_app():
	app = Flask(__name__)
	app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
		os.path.join(base_dir, 'blog.db')
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	app.config["SECRET_KEY"] = 'iLhqyLO3HtSpsE8cuQaj'
	app.config["SECRET_KEY"] = 'blog'
	db.init_app(app)


	@app.before_first_request
	def create_tables():
			db.create_all()

	login_manager = LoginManager()
	login_manager.login_view = "Users.login"
	login_manager.init_app(app)

	def __repr__(self):
		return f"User <{self.username}"

	@login_manager.user_loader
	def user_loader(id):
		return UserModel.query.get(int(id))

	app.register_blueprint(AvenBlueprint)
	app.register_blueprint(ArticleBlueprint)
	app.register_blueprint(UserBlueprint)

	return app

if __name__=="__main__":
	app = create_app()
	app.run(debug=True)
