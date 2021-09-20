from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id): 
  return User.query.get(int(user_id))

# User model
class User(UserMixin,db.Model): 
  __tablename__ = 'users' #name of table in pitch database
  
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  user_email = db.Column(db.String(255),unique = True,index = True)
  biodata = db.Column(db.String)
  profile_pic_path = db.Column(db.String)
  user_password = db.Column(db.String(255))
  
  pitches = db.relationship('Pitches',backref = 'user', lazy = "dynamic")
  comments = db.relationship('Comments',backref = 'user', lazy = "dynamic")
  
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password): #Generating a hashed password
    self.user_password = generate_password_hash(password)
    
  def verify_password(self,password): #Confirming whether the hashed password is similar to the one entered
    return check_password_hash(self.user_password,password)
  
  def __repr__(self): 
    return f'User {self.username}'
  
# Pitches model
class Pitches(db.Model): 
  __tablename__ = 'pitches' #name of table in pitch database
  
  id = db.Column(db.Integer,primary_key = True)
  pitch_category = db.Column(db.String(255))
  pitch_title = db.Column(db.String(255))
  pitch = db.Column(db.String) #no maximum length:depends on input
  submitted = db.Column(db.DateTime,default=datetime.utcnow)
  
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  comments = db.relationship('Comments', backref = 'pitches', lazy = "dynamic")
  upvote = db.relationship('Upvote', backref='pitches', lazy='dynamic')
  downvote = db.relationship('Downvote', backref='pitches', lazy='dynamic')
    
  def save_pitch(self):
    '''Method to save  submitted pitches'''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches(cls,category):
    '''Method to retrieve pitches according to category'''
    pitches = Pitches.query.filter_by(pitch_category = category).all()
    return pitches
  
  def __repr__(self): 
    return f'User {self.pitch_category}'
  
# Comments model
class Comments(db.Model): 
  __tablename__ = 'comments' #name of table in pitch database
  
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String)
  submitted = db.Column(db.DateTime,default=datetime.utcnow)
  
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
  
  def save_comment(self):
    '''Method to save  submitted comments for each pitch'''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    '''Method to retrieve comments for specific pitches in different categories'''
    comments_by_id = Comments.query.filter_by(pitch_id = id).all()
    return comments_by_id
  
  def __repr__(self): 
    return f'User {self.comment} > {self.pitch_id}'
  
#votes
  
class Upvote(db.Model):
  __tablename__ = 'upvotes'

  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_upvotes(cls,pitch_id):
    upvote = Upvote.query.filter_by(pitch_id=pitch_id).all()

    return upvote

  def __repr__(self):
    return f'Pitch id:{self.pitch_id}'

class Downvote(db.Model):
  __tablename__ = 'downvotes'

  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_downvotes(cls,pitch_id):
    downvote = Downvote.query.filter_by(pitch_id=pitch_id).all()

    return downvote

  def __repr__(self):
    return f'Pitch id:{self.pitch_id}'