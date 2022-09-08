import click
from flask.cli import with_appcontext

from .extensions import flask_db


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    flask_db.create_all()