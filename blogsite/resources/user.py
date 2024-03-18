from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
# from flask_smorest import Blueprint, abort
from db import db
from blogsite.models import UserModel
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("Users", "user", __name__)


# signup route
@auth.route('/signup', methods = ['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form.get('username')
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		email = request.form.get('email')
		password = request.form.get('password')
		confirm_password = request.form.get('confirm_password')

		password_hash = generate_password_hash(password)
		email_exists = UserModel.query.filter_by(email=email).first()
		if email_exists:
			flash('This mail already exists!', category='error')
		elif password != confirm_password:
			flash('Password does not match.', category='error')
		elif len(password) < 8:
			flash('Password is too short.', category='error')
		elif len(email) < 5:
			flash('Invalid email.', category='error')
		else:
			new_user = UserModel(firstname=firstname, lastname=lastname, username = username, email = email, password_hash = password_hash)
			db.session.add(new_user)
			db.session.commit()
			flash('Your account has been created!')
			login_user(new_user, remember=True)

			return redirect(url_for('aven.index'))

	return render_template('register.html')



@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = UserModel.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash(f"Good to have you back, {user.username}", category='success')
                login_user(user, remember=True)
                return redirect(url_for('aven.index'))
            else:
                flash("Incorrect password!", category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")




@auth.route('/logout')
def logout():
	logout_user()
	flash('Logout successful')
	return redirect(url_for('aven.index'))













