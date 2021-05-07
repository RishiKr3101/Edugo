from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/',methods=["POST", "GET"])
def login():
    if request.method == 'POST' :
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email= email).first()
        if user:
            if check_password_hash(user.password, password):
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
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

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
            new_user = User(email=email, first_name=first_name, password= generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))


    else:
        return render_template("signup.html")


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"