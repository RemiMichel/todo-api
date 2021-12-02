import simplejson

from src.dao.dao import Dao
from src.todo import Todo
from flask import jsonify


class Json(Dao):

    def __init__(self):
        self.todos = {}
        f = open("db.json", "r")
        json = f.read()
        array = simplejson.loads(json)
        if array:
            for todo_json in array:
                todo = Todo(todo_json["label"])
                todo.id = todo_json["id"]
                todo.status = todo_json["status"]
                self.todos[todo_json['id']] = todo

    def get(self, todo_id):
        return self.todos[todo_id].serialize()

    def create(self, label):
        todo = Todo(label)
        todo.id = len(self.todos)
        self.todos[todo.id] = todo
        self.write()
        return todo.serialize()

    def update(self, todo_id, label, status):
        todo = self.todos[todo_id]
        todo.label = label
        todo.status = int(status)
        self.todos[todo.id] = todo
        self.write()
        return todo.serialize()

    def list(self):
        return jsonify(self.get_serialized_todos())

    def write(self):
        f = open("db.json", "w")
        f.write(simplejson.dumps(self.get_serialized_todos()))
        f.close()

    def get_serialized_todos(self):
        serialized_todos = []
        for todo_id in self.todos:
            serialized_todos.append(self.todos[todo_id].serialize())
        return serialized_todos
