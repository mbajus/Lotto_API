import os 

SQLALCHEMY_DATABASE_URI = "postgresql://ukjqjsatnawsnr:f717d4c1a574882a1589dfb9f070a7bb5ff568277dda1464a4a18fe0216c6ae6@ec2-34-241-90-235.eu-west-1.compute.amazonaws.com:5432/delug4lrrcpmt8"
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False