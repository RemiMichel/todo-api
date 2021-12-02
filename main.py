from flask import Flask
from flask_restful import Api
from config import db
from src.resources import TodoResource, TodoListResource

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
api = Api(app)

api.add_resource(TodoListResource, '/todos')
api.add_resource(TodoResource, '/todo/<int:todo_id>')


@app.route('/')
def index():
    return "Hello world !"


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
