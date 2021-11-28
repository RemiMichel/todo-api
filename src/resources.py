from flask import jsonify
from flask_restful import Resource, reqparse
from config import db
from src.model import Todo

parser = reqparse.RequestParser()
parser.add_argument('label')
parser.add_argument('status')


class TodoResource(Resource):
    def get(self, todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        return todo.serialize()

    def put(self, todo_id):
        args = parser.parse_args()
        label = args["label"]
        status = args["status"]
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.label = label
        todo.status = status
        db.session.commit()
        return todo.serialize()


class TodoListResource(Resource):
    def get(self):
        todos = Todo.query.all()
        serialized_todos = []
        for todo in todos:
            serialized_todos.append(todo.serialize())
        return jsonify(serialized_todos)

    def post(self):
        args = parser.parse_args()
        label = args["label"]
        todo = Todo(label)
        db.session.add(todo)
        db.session.commit()
        return todo.serialize()


class TodoListStatusResource(Resource):
    def get(self, status):
        todos = Todo.query.filter_by(status=status).all()
        serialized_todos = []
        for todo in todos:
            serialized_todos.append(todo.serialize())
        return jsonify(serialized_todos)
