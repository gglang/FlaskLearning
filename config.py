import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # For security, this key should be a hard to guess value set in 
    # the environment variables; for dev purposes, 'or' coalesces it here
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-wouldnt-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['gerald.devbot@gmail.com']
    LANGUAGES = ['en', 'fr']
    POSTS_PER_PAGE = 25
