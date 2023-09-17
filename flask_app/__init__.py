import os
from flask_app.config import Config
from flask import Flask
from flask_assets import Bundle, Environment



def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)

    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css")

    from flask_app.main.routes import main
    app.register_blueprint(main)
    assets.register("css", css)
    css.build()

    return app