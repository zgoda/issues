from flask import Flask, jsonify
from flask_restful import Api

from .ext import api, pony
from .resource import TodoCollectionResource


def make_app():
    app = Flask(__name__.split('.')[0])

    @app.route('/')
    def index():
        return jsonify({'message': 'Hello Flask-RESTFul'})

    configure_extensions(app)

    return app


def configure_extensions(app):
    pony.init_app(app)
    api.init_app(app)
    configure_resources(api)


def configure_resources(api: Api):
    api.add_resource(TodoCollectionResource, '/todos')
