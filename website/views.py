from flask import Blueprint, app, render_template, redirect,request, jsonify, make_response, Response
from flask_login import login_required, current_user
from .models import Comments, User, Posts, Likes
from . import db
import json
from base64 import b64encode

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    
    print(current_user)
    if request.method == 'POST':
        post = request.form.get('post')
        post=post.replace("[sp]", "&nbsp;")
        post=post.replace("[n1]", "\n")
        print(post)

        if len(post)<1:
            return render_template("home.html", user=current_user)
        
        else:
            new_post = Posts(data=post, user_id = current_user.id)
            
            db.session.add(new_post)
            db.session.commit()


    
    return render_template("home.html", user=current_user)



@views.route('/feeds', methods= ['GET','POST'])
@login_required
def timeline():
    

    posts_liked=[]
    
    for likes in Likes.query.all() :
        if current_user.id == likes.user :
            posts_liked.append(likes.post_id)
    
    return render_template("timeline.html", user=current_user, posts=Posts.query.all(), user_list=User.query.all(), likes= posts_liked)



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


@views.route('/like-post', methods= ['POST'])
def like_post():
    
    like = json.loads(request.data)
    
    postId = like['PostId']
    
    posts=Posts.query.all()
    for post in posts :
        if post.id == postId:
            post.no_of_likes += 1
    
    
    like = Likes(user=current_user.id , post_id= postId)
    
    db.session.add(like)
    db.session.commit()
    
    return jsonify({})


@views.route('/dislike-post', methods= ['POST'])
def dislike_post():
    
    dislike = json.loads(request.data)
    
    postId = dislike['PostId']
    
    posts=Posts.query.all()
    for post in posts :
        if post.id == postId:
            for like in post.likes :
                if(current_user.id == like.user):
                    db.session.delete(like)
                    post.no_of_likes -= 1
                    db.session.commit()
            
    

    
    
    return jsonify({})

@views.route('/comment', methods= ['POST'])
def comment():
    
    comments = json.loads(request.data)
    
    postId, data = comments['PostId'] , comments['data']
    
    posts=Posts.query.all()
    for post in posts :
        if post.id == postId:
            post.no_of_comments += 1
    
    
    comment = Comments(user=current_user.id , data= data , post_id= postId)
    
    db.session.add(comment)
    db.session.commit()
    
    return jsonify({})


@views.route('/remove-comment', methods= ['POST'])
def remove_comment():
    
    comment = json.loads(request.data)
    
    postId = comment['PostId']
    
    posts=Posts.query.all()
    for post in posts :
        if post.id == postId:
            for comment in post.comments :
                if(current_user.id == comment.user):
                    db.session.delete(comment)
                    post.no_of_comments -= 1
                    db.session.commit()
            
    

    
    
    return jsonify({})

@views.route('/profilepic/<int:id>')
def profilepic(id):
    event = User.query.filter_by(id=id).first()
    print("hey")
    image=b64encode(event.profile_pic)
    return (image)