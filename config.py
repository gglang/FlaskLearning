import os


class Config(object):
    # For security, this key should be a hard to guess value set in 
    # the environment variables; for dev purposes, 'or' coalesces it here
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-wouldnt-guess'
