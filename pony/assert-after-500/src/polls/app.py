from flask import Flask, jsonify

from .ext import pony
from .models import Poll


def make_app():
    app = Flask(__name__.split('.')[0])

    @app.route('/')
    def index():
        return jsonify({'message': 'Hello Pony'})

    @app.route('/unhandled')
    def unhandled():
        polls = [
            p.to_dict(with_collections=True) for p in Poll.select().order_by(Poll.x)
        ]
        return jsonify(polls)

    configure_extensions(app)
    return app


def configure_extensions(app):
    pony.init_app(app)
