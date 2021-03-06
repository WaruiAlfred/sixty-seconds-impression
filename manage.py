from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitches,Comments
from flask_migrate import Migrate,MigrateCommand

# App instance created
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test(): 
  '''Run the unit tests.'''
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

#flask-script shell
@manager.shell
def make_shell_context(): 
  return dict(app = app, db = db, User = User, Pitches = Pitches, Comments = Comments)

# Setting up Flask-Migrate to create a new database schema
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__': 
  manager.run()