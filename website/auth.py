from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)


@auth.route('/',methods=["POST", "GET"])
def login():
    return render_template("login.html")


@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)< 4:
            flash('Email error', category='error')
        elif len(firstName)< 2:
            flash('Name error', category='error')
        elif password1 != password2:
            flash ('password not matching', category='error')
        elif len(password1) <7:
            flash('password short', category='error')
        else:
            flash('Account created', category='success')




    return render_template("signup.html")


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"