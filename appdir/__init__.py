from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['DIRECT_SECRET_KEY'] = 'you-will-never-guess'
app.config.from_object(Config)

# print(app.config)

global global_string
global_string = 'Testing Global Variable!!!'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from appdir import routes, models
