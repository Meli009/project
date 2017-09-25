import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktask.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI	= 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS=True

DEBUG = True

