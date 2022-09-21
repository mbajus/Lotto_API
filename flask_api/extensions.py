from flask_sqlalchemy import SQLAlchemy as FlaskSQL
from sqlalchemy import create_engine

from .models import metadata
from .settings import SQLALCHEMY_DATABASE_URI


flask_db = FlaskSQL(metadata=metadata) # connection for flask

db = create_engine(SQLALCHEMY_DATABASE_URI) # engine for update