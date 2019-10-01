from flask import Blueprint, request

from app.modules.decorators.responseformat import FormatResponse
from .dal import TodoDAL

todo_module = Blueprint('todo', __name__, url_prefix="/v1/todos")

datalayer = TodoDAL()


@todo_module.route("")
@FormatResponse
def get_all_todos():
    return {
        'todos': datalayer.get_all_todos()
    }


@todo_module.route("/<todoid>")
@FormatResponse
def get_todo_by_id(todoid):
    return {
        'todos': datalayer.get_todo_by_id(todoid)
    }


@todo_module.route("/save", methods=[ 'POST' ])
@FormatResponse
def add_todo():
    return {
        'todos': datalayer.add_todo_item(dict(request.json))
    }
