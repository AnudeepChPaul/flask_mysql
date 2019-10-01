from flask import Flask, abort, request

from app.db import db
from app.modules import init_module

app = Flask(__name__)

# loads all the modules and related routes
init_module(app)


@app.errorhandler(404)
def error(Response):
    return { 'message': 'Not Found' }, 404


@app.errorhandler(400)
def error(Response):
    return { 'message': 'Not Found' }, 400


@app.before_request
def verify_access_token():
    token = request.headers.get('X-ACCESS-TOKEN')
    if token is None or len(token) == 0:
        abort(403)
