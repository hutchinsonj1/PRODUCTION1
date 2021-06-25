from flask import Flask
from .extensions import db
from .routes import shortener

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(shortener)

    return app

#also passing the 'config_file' to the flask function