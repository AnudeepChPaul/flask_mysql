from app.modules.todos import todo_module


def init_module(app):
    app.register_blueprint(todo_module)
