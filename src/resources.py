from flask_restful import Resource, reqparse
from src.dao.mysql import Mysql

dao = Mysql()

parser = reqparse.RequestParser()
parser.add_argument('label')
parser.add_argument('status')


class TodoResource(Resource):
    def get(self, todo_id):
        return dao.get(todo_id)

    def put(self, todo_id):
        args = parser.parse_args()
        label = args["label"]
        status = args["status"]
        return dao.update(todo_id, label, status)


class TodoListResource(Resource):
    def get(self):
        return dao.list()

    def post(self):
        args = parser.parse_args()
        label = args["label"]
        return dao.create(label)
