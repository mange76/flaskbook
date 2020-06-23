import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '665eaf2a-6bdb-4d17-a987-e9a7afa7081f'
