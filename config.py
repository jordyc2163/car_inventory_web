import os

basedir = os.path.abspath(os.path.dirname(__file__))
# gives access to the project in any OS we find ourselves in
# Allows outside files/folders to be added to the project from the base directory

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SOMETHING'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False #turns off updates messages from sqlalchemy