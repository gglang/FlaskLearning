import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # For security, this key should be a hard to guess value set in 
    # the environment variables; for dev purposes, 'or' coalesces it here
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-wouldnt-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False