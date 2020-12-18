from flask import Flask

from tools.config import DevelopmentConfig, ProductionConfig, TestingConfig

#Create Flask object
def create_app(config_object=DevelopmentConfig()):
    app = Flask(__name__)
    app.config.from_object(config_object)

    from routes import bp as routes
    app.register_blueprint(routes)
    return app
