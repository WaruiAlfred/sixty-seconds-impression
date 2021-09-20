import os

class Config: 
  '''
  General configuration class
  '''
  SECRET_KEY = os.environ.get("SECRET_KEY") #secret key for wtf forms
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:@localhost/pitch'
  UPLOADED_PHOTOS_DEST = 'app/static/photos' #storage location of uploaded photos in the app
  
#  app email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config): 
  '''
  Production configuration child class
  '''
  pass

class DevConfig(Config): 
  '''
  Development configuration child class
  '''
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production': ProdConfig
}