import click
from flask.cli import with_appcontext

from .extensions import flask_db

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    flask_db.create_all()

@click.command(name='recreate_tables')
@with_appcontext
def recreate_tables():
    tables = flask_db.metadata.tables.keys()
    for table in tables:
        flask_db.session.execute(f'DROP TABLE IF EXISTS {table};')
    flask_db.create_all()
    print('RESTART DATABASE - All tables are recreated.')