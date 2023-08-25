from flask import Flask
from .Modelos import db, cancion, medio, album, usuario

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial_canciones.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
