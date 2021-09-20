import unittest 
from app.models import Pitches,User,Comments
from app import db
 
class CommentsTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the Comments class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.user_aldis = User(username = 'Aldis', user_email = 'aldis@gmail.com',password = 'aldis')
    self.new_pitch = Pitches(pitch_category="Game pitch",pitch_title='FIFA',pitch="This is a game for upcoming footballers.",user = self.user_aldis )
    self.new_comment = Comments(comment="That's a game i'll have to try out.",user_id = self.user_aldis.id ,pitch_id = self.new_pitch.id)
    
  
  def test_instance(self): 
    self.assertTrue(isinstance(self.new_comment,Comments))
    