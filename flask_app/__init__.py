import os
from flask_app.config import Config
from flask import Flask
from flask_assets import Bundle, Environment



def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)

    assets = Environment(app)
    css = Bundle("src/main.css", output="dist/main.css")
    js = Bundle("src/*.js", output="dist/main.js")

    from flask_app.main.routes import main
    from flask_app.api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api)

    assets.register("css", css)
    assets.register("js", js)
    css.build()
    js.build()

    return app