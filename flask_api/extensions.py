from flask_sqlalchemy import SQLAlchemy as FlaskSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import metadata
from .settings import SQLALCHEMY_DATABASE_URI


flask_db = FlaskSQL(metadata=metadata) # connection for flask

db = Session(create_engine(SQLALCHEMY_DATABASE_URI)) # connection for update