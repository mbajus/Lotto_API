import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1) # sqlalchemy doesnt support postgres, insted od postgresql
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEYS = False