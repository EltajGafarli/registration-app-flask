from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask('__main__',template_folder='app/templates',static_folder='app/static')

app.secret_key = 'eltaj'

db = SQLAlchemy(app=app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:190407011@localhost:5432/registration'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app=app)

login_manager = LoginManager(app=app)

from app import routes