from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import db
from src.resources import TodoResource, TodoListResource

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

migrate = Migrate(app, db)

api = Api(app)

api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todo/<int:todo_id>')


@app.route('/')
def index():
    return "Everything works fine !"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    db.create_all()
