from flask import Flask 

from .commands import create_tables, complete_update_db, last_update_db
from .extensions import flask_db
from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    flask_db.init_app(app)
    app.register_blueprint(main)

    app.cli.add_command(create_tables)
    app.cli.add_command(complete_update_db)
    app.cli.add_command(last_update_db)

    return app


