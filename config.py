from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

SECRET_KEY = "This is a secret key"
SQLALCHEMY_TRACK_MODIFICATIONS = "false"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@host/todo"