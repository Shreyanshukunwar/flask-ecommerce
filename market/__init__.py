from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configs for db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)

from market import routes