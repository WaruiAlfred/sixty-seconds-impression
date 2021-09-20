import unittest 
from app.models import User 

class UserModelTest(unittest.TestCase): 
  
  def setUp(self):
    '''
    method that creates an instance of  User class 
    '''
    self.new_user = User(password = 'aldis')
    
  def test_password_input(self): 
    '''
    this ascertains that when password is being hashed,the user_password contains a value
    '''
    self.assertTrue(self.new_user.user_password is not None)
    
  def test_no_password_access(self): 
    '''
    taste case confirms that the application raises an AttributeError when one tries to access the password property
    '''
    with self.assertRaises(AttributeError): 
      self.new_user.password
    
  def test_password_verification(self): 
    '''
    test confirms that the password_hash can be verified when a correct password is passed in
    '''
    self.assertTrue(self.new_user.verify_password('aldis'))