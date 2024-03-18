# contain all the routes
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, current_user
from blogsite.models import ArticleModel, UserModel, CommentModel
from db import db

aven = Blueprint("aven", __name__)


@aven.route("/")
@aven.route("/index")
def index():
	articles = ArticleModel.query.all()
	return render_template("index.html", user=current_user, articles=articles,  )


@aven.route("/article/<int:article_id>")
def view_article(article_id):
    article = ArticleModel.query.get(article_id)
    if article:
        comments = CommentModel.query.filter_by(article_id=article_id).all()
        for comment in comments:
            comment.author_username = UserModel.query.get(comment.author).username
            print(comments)
        return render_template("view_article.html", article=article, comments=comments)
    else:
        flash("Article not found.", category="error")
        return redirect(url_for("index"))


@aven.route("/publish", methods=['GET', 'POST'])
@login_required
def publish():
	if request.method == "POST":
		title = request.form.get('title')
		bodytext = request.form.get('bodytext')

		if not bodytext and not title:
			flash('Please fill in the Title and Bodytext fields to proceed')
		else:
			article = ArticleModel(title=title, bodytext=bodytext, author=current_user.id)
			db.session.add(article)
			db.session.commit()
			flash("Your article has been successfully published", category='success')
			return redirect(url_for('aven.index'))
	return render_template('publish.html')







@aven.route("/article/<email>")
@login_required
def aricles(email):
    user = UserModel.query.filter_by(email=email).first()

    if not user:
        flash('No user with that email exists.', category='error')
        return redirect(url_for('index'))

    aricles = user.aricles
    return render_template("aricles.html", user=current_user, aricles=aricles, email=email)






