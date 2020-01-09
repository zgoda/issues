from flask.cli import FlaskGroup
from dotenv import find_dotenv, load_dotenv

from .app import make_app


def create_app(info):
    return make_app()


cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    cli()
