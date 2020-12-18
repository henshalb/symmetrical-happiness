from flask import Flask
from .config import Config

def create_app(debug=False):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = debug
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app