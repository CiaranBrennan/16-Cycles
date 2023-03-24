import os
from decouple import config

WTF_CSRF_ENABLED = False
SECRET_KEY = config("SECRET_KEY")

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = '16cyclesreset@gmail.com'
MAIL_PASSWORD = '16cyclespword'


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
