import os

class FlaskConfig(object):
    FLASK_DEBUG = False
    TESTING  =  False
    SECRET_KEY = os.environ['SECRET_KEY']

class DevelopmentConfig(FlaskConfig):
    FLASK_DEBUG = True

class ProductionConfig(FlaskConfig):
    pass

class TestingConfig(FlaskConfig):
    pass
