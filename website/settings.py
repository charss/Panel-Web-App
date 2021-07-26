import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://wqnesjbiyaczbc:d2969f9243a69e5a09ce38b4027ea591f5c23f0539a38f78707344960553ab9b@ec2-54-147-93-73.compute-1.amazonaws.com:5432/dd96mmb8m0errj')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False