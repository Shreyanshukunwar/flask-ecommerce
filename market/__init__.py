from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#Configs for db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '542999b3772800fd586b0ee4'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from market import routes