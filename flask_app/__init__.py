import os
from flask_app.config import Config
from flask import Flask


def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)

    from flask_app.main.routes import main
    app.register_blueprint(main)

    return app