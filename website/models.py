from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import PickleType
from sqlalchemy.dialects.sqlite import BLOB


class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user= db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    no_of_likes = db.Column(db.Integer, default= 0)
    likes = db.relationship('Likes', backref='author', lazy=True)


class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    posts = db.relationship('Posts', backref='author', lazy=True)