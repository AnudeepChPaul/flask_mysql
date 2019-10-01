from app.db import db
from app.utils.dictionize import Dictionize

GET_ALL_TODOS = 'SELECT * FROM `flask`.`todo`'


class TodoDAL:
    def __init__(self):
        self.db = db

    def get_all_todos(self):
        cursor = self.db.cursor()
        cursor.execute(GET_ALL_TODOS)
        return [ todo for todo in Dictionize(cursor) ]

    def get_todo_by_id(self, todoid):
        cursor = self.db.cursor()
        cursor.execute('select * from todo where id = "{}"'.format(todoid))
        return [ todo for todo in Dictionize(cursor) ]

    def add_todo_item(self, todo):
        cursor = self.db.cursor()
        query = 'insert into flask.todo (name, description, content) VALUES ("{}", "{}", "{}");'.format(
            todo[ 'name' ], todo[ 'description' ], todo[ 'content' ]
        )
        cursor.execute(query)
        res = cursor.fetchone()
        return [ todo for todo in Dictionize(cursor) ]
