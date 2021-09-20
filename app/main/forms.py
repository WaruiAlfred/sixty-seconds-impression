from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm): #update profile form
  bio = TextAreaField('Tell us about yourself.',validators=[Required()])
  submit = SubmitField('Submit')
  
class PitchForm(FlaskForm): #form for submitting pitches
  pitch_category = SelectField('Pitch Category', choices=[('Project pitch', 'Project pitch'), ('Game pitch', 'Game pitch'), ('Pick-up lines', 'Pick-up lines'), ('Interview pitch','Interview pitch')],validators=[Required()])
  pitch_title = StringField('Pitch title',validators=[Required()])
  pitch = TextAreaField('Type in your pitch.',validators=[Required()])
  submit = SubmitField('Submit')
  
class CommentsForm(FlaskForm): #form for submitting comments for different pitches
  comment = TextAreaField('Leave a comment.',validators=[Required()])
  submit = SubmitField('Submit')