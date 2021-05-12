from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/',methods=["POST", "GET"])
def login():
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email= email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return render_template("login.html")
        else:
            return render_template("login.html")

    return render_template("login.html")


@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        profile_pic= request.files.get("profilepic")

        user = User.query.filter_by(email= email).first()
        if user:
            return render_template("signup.html")

        if len(email)< 4:
            flash('Email error', category='error')
        elif len(first_name)< 2:
            flash('Name error', category='error')
        elif password1 != password2:
            flash ('password not matching', category='error')
        elif len(password1) <7:
            flash('password short', category='error')
        else:
            new_user = User(email=email, username=username  , first_name=first_name, profile_pic=profile_pic, password= generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email= email).first()
            login_user(user, remember=True)
            return redirect(url_for('views.home'))


    else:
        return render_template("signup.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))