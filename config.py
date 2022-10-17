from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

config = dotenv_values(".env")

db = SQLAlchemy()

SECRET_KEY = config["SECRET_KEY"]
SQLALCHEMY_TRACK_MODIFICATIONS = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
SQLALCHEMY_DATABASE_URI = config["SQLALCHEMY_DATABASE_URI"]