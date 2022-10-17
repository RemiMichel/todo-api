FROM python:3

RUN pip install Flask
RUN pip install flask_sqlalchemy
RUN pip install Flask-Migrate
RUN pip install flask_restful

RUN pip install pymysql
RUN pip install simplejson
RUN pip install cryptography
RUN pip install python-dotenv

COPY . /app

RUN export FLASK_APP="/app/main.py"