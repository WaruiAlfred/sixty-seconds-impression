import unittest 
from app.models import Pitches,User
from app import db
 
class PitchesTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the Review class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.user_aldis = User(username = 'Aldis', user_email = 'aldis@gmail.com',password = 'aldis')
    self.new_pitch = Pitches(pitch_category="Game pitch",pitch_title='FIFA',pitch="This is a game for upcoming footballers.",user = self.user_aldis )
    
  
  def test_instance(self): 
    self.assertTrue(isinstance(self.new_pitch,Pitches))
    
  def test_check_instance_variables(self):
    self.assertEquals(self.new_pitch.pitch_category,"Game pitch")
    self.assertEquals(self.new_pitch.pitch_title,'FIFA')
    self.assertEquals(self.new_pitch.pitch,"This is a game for upcoming footballers.")
    self.assertEquals(self.new_pitch.user,self.user_aldis,'1')
    