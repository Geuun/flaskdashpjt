from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IEEEDB.db'
app.config['SECRET_KEY'] = 'QMWKEFMLKQWEJFISOAKSDFLAOEFLWFMKWEL12312ASKDFLWEM123ASK'

db = SQLAlchemy(app)

from application import routes