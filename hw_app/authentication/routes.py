from crypt import methods
from flask import Blueprint, render_template, request, redirect, url_for, flash
from hw_app.forms import UserSignUpForm, UserSignInForm

from hw_app.models import User, db, check_password_hash

from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserSignInForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were succesfully logged in.', 'auth-success')
                return redirect(url_for('site.profile'))
            else:
                flash('Email or Password is incorrect. Try again', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form')

    return render_template('signin.html', form=form)


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignUpForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data

            user = User(email, first_name, last_name, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f"You have succesfully created a user account {email}", 'user-created')

            return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form') 
    return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))