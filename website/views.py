from flask import Blueprint, render_template, redirect,request, jsonify
from flask_login import login_required, current_user
from .models import User, Posts
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    
    print(current_user)
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post)<1:
            return render_template("home.html", user=current_user)
        
        else:
            new_post = Posts(data=post, user_id = current_user.id)
            
            db.session.add(new_post)
            db.session.commit()


    
    return render_template("home.html", user=current_user)



@views.route('/feeds')
@login_required
def timeline():
    
    return render_template("timeline.html", user=current_user, posts=Posts.query.all(), user_list=User.query.all())



@views.route('/remove-post', methods= ['POST'])
def remove_post():
    post = json.loads(request.data)
    postId = post['PostId']
    post = Posts.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()
    
    return jsonify({})