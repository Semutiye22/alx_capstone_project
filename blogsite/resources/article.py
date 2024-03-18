from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, current_user
from blogsite.models import ArticleModel, UserModel, CommentModel
from db import db


article = Blueprint("Article", "article", __name__)



@article.route("/edit/<article_id>", methods=['GET', 'POST'])
@login_required
def edit(article_id):
	article = ArticleModel.query.filter_by(id=article_id).first()
	if request.method == 'POST':
		title = request.form.get('title')
		bodytext = request.form.get('bodytext')

		if not article:
			flash("We can't find your article, Try creating and publising one.", category='error')
		elif current_user.id != article.author:
			flash("You are not allowed to make changes to this article.", category='error')
		else:
			article.title = title
			article.bodytext = bodytext
			db.session.commit()
			flash('You successfully edited this article', category='success')
		return redirect(url_for('aven.index'))
	return render_template('edit.html', article=article)


@article.route('/delete/<article_id>')
@login_required
def delete(article_id):
	article = ArticleModel.query.filter_by(id=article_id).first()

	if not article:
                        
		print("This article does not exist.", category='error')
	elif current_user.id != article.author:
		flash('You are not allowed to delete this article', category='error')
	else:
		db.session.delete(article)
		db.session.commit()
		flash('You have deleted this article', category='success')
	return redirect(url_for('aven.index'))


@article.route("/articles/<username>")
@login_required
def articles(username):
    user = UserModel.query.filter_by(username=username).first()

    if not user:
        flash('This user does not exist.', category='error')
        return redirect(url_for('aven.index'))

    articles = user.articles
    return render_template("article.html", user=current_user, articles=articles, username=username)



@article.route("/create-comment/<article_id>", methods=['GET','POST'])
@login_required
def create_comment(article_id):
    text = request.form.get('text')

    if not text:

        flash('Comment cannot be empty.', category='error')
    else:
        article = ArticleModel.query.filter_by(id=article_id)
        
        if article:

            print("--+++++---")
            print(text)

            comment = CommentModel(
                text=text, author=current_user.username, article_id=article_id)
            print(comment.text)
            db.session.add(comment)
            db.session.commit()
        else:
            print("+============")
            flash('Article does not exist.', category='error')

    return redirect(url_for('aven.index'))


@article.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = CommentModel.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.author and current_user.username != comment.article.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('aven.index'))
