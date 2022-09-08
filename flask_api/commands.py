import click
from flask.cli import with_appcontext

from .extensions import flask_db
from .datascraper.main import update, lastupdate


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    flask_db.create_all()

@click.command(name='complete_update_db')
@with_appcontext
def complete_update_db():
    update()

@click.command(name='last_update_db')
@with_appcontext
def last_update_db():
    lastupdate()

