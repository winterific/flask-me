from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


@app.route('/', methods=['get'])
def get_it():
    # raise Exception('I fed up!')
    return dict(message='hi!')


@app.route('/', methods=['post'])
def post_it():
    content_type = request.headers.get('content-type', 'text/plain')
    body = request.get_data()
    return body, 200, {'Content-Type': content_type}


@app.errorhandler(HTTPException)
def http_error(err):
    return dict(errors=[err.description]), err.code


@app.errorhandler(Exception)
def error(err):
    return dict(errors=err.args), 500
