from flask import Blueprint, render_template, redirect,request
from flask_login import login_required, current_user
from .models import User, Posts
from . import db


views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post)<1:
            return render_template("home.html")
        
        else:
            new_post = Posts(data=post, user_id = current_user.id)
            db.session.add(new_post)
            db.session.commit()


    
    return render_template("home.html", user=current_user)