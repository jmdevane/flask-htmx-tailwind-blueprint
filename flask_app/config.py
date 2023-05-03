import os

class Config:

    SECRET_KEY = os.environ['FLASK_SECRET_KEY']