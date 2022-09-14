import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('AWS_DATABASE', 'postgresql://dbadmin:DOuJCmcliCYR0MeVxEfZ@lottery-database.c4oeaaldfp8m.us-east-1.rds.amazonaws.com:5432/lotto')
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEYS = False