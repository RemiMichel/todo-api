from config import db
from src.dao.dao import Dao
from src.todo import Todo
from flask import jsonify


class Mysql(Dao):

    def get(self, id):
        return Todo.query.filter_by(id=id).first()

    def create(self, label):
        todo = Todo(label)
        db.session.add(todo)
        db.session.commit()
        return todo.serialize()

    def update(self, id, label, status):
        todo = Todo.query.filter_by(id=id).first()
        todo.label = label
        todo.status = status
        db.session.commit()
        return todo.serialize()

    def list(self):
        todos = Todo.query.all()
        serialized_todos = []
        for todo in todos:
            serialized_todos.append(todo.serialize())
        return jsonify(serialized_todos)
