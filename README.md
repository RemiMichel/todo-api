# todo-api
An api for Todo management in Python


### Docker-compose

in case you don't want to use docker-compose, you have to change SQLALCHEMY_DATABASE_URI in the config.py file otherwise just docker-compose up the .yml file

### To set up :
```
virtualenv env -p python3
. env/bin/activate
pip install flask 
pip install flask_sqlalchemy
pip install pymysql
pip install flask_restful
pip install simplejson (use to store data in json file)
```
### Run :
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

### DAO

to use mysql :
_(resources.py)_
```
from src.dao.mysql import Mysql
dao = Mysql()
```
to use json file :
_(resources.py)_
```
from src.dao.json import Json
dao = Json()
```