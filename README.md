# todo-api
An api for Todo management in Python

### To set up :
```
virtualenv env -p python3
. env/bin/activate
pip install flask 
pip install flask_sqlalchemy
pip install pymysql
pip install flask_restful
```
### To run :
```
python main.py
```

**If you are working with pycharm.**  
You have to update the python interpreter to use the virtual env   
_File > Settings > Project: todo-api > Python interpreter_  
Otherwise you have to install flask on your device

### Requests

```
GET http://127.0.0.1:5000/todos
POST http://127.0.0.1:5000/todos
{"label": "yourLabel"}
GET http://127.0.0.1:5000/todo/4
PUT http://127.0.0.1:5000/todo/4
{"label": "updatedLabel", "status": 0}
```