import flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)