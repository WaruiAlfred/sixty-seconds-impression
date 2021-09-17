from flask import render_template
from . import main

# Views functions
@main.route('/')
def  index():
  '''
  Function that returns the home page
  '''
  title = "Impression in 60 seconds"
  return render_template('index.html',title = title)

@main.route('/game')
def  gamepitch():
  '''
  Function that returns data displayed in the gamepitch template
  '''
  title = "Impression in 60 seconds-gamepitch"
  return render_template('pitch-categories/game.html',title = title)

@main.route('/interview')
def  interviewpitch():
  '''
  Function that returns the data of interview pitch 
  '''
  title = "Impression in 60 seconds-interviewpitch"
  return render_template('pitch-categories/interview.html',title = title)

@main.route('/pickuplines')
def  pickuplinespitch():
  '''
  Function that returns pickuplines contents
  '''
  title = "Impression in 60 seconds-pickuplinespitch"
  return render_template('pitch-categories/pickuplines.html',title = title)

@main.route('/project')
def  projectpitch():
  '''
  Function that returns the projectpitch page and its contents
  '''
  title = "Impression in 60 seconds-projectpitch"
  return render_template('pitch-categories/project.html',title = title)