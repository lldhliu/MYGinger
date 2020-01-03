"""
 Created by 刘大怪 on 20-1-3
"""
from flask import Flask

__author__ = "刘大怪"


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)

    return app
