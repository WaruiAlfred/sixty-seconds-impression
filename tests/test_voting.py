import unittest 
from app.models import Pitches,Upvote,Downvote,User
from app import db
 
class VotingTest(unittest.TestCase): 
  '''Test class to test the behaviour of upvote class'''
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.user_aldis = User(username = 'Aldis', user_email = 'aldis@gmail.com',password = 'aldis')
    self.new_pitch = Pitches(pitch_category="Game pitch",pitch_title='FIFA',pitch="This is a game for upcoming footballers.",user = self.user_aldis )
    self.new_upvote = Upvote(pitch_id = self.new_pitch.id)
    self.new_downvote = Downvote(pitch_id = self.new_pitch.id)
  
  def test_instance(self): 
    self.assertTrue(isinstance(self.new_upvote,Upvote))
    self.assertTrue(isinstance(self.new_downvote,Downvote))
    
  def test_check_instance_variables(self):
    self.assertEquals(self.new_upvote.pitch_id,self.new_pitch.id)
    self.assertEquals(self.new_downvote.pitch_id,self.new_pitch.id)
    