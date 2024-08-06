from flask import Flask
from .routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register the main blueprint
    app.register_blueprint(main_blueprint)

    return app
