import click
from flask.cli import with_appcontext

from .extensions import db
from .datascraper.main import update, lastupdate


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

@click.command(name='completeupdate')
@with_appcontext
def db_complete_update():
    update()

@click.command(name='lastupdate')
@with_appcontext
def db_last_update():
    lastupdate()

