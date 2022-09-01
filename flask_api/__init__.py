from flask import Flask 

from .commands import create_tables, getpage, dbrecords, updatedb
from .extensions import db
from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(main)

    app.cli.add_command(create_tables)
    app.cli.add_command(updatedb)
    app.cli.add_command(dbrecords)

    return app


