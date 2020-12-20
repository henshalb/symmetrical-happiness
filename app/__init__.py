from flask import Flask
from flask.templating import render_template
from .config import Config

# error handler
def page_not_found(e):
  return render_template('404.html'), 404

def create_app(debug=False):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = debug
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.register_error_handler(404, page_not_found)
    return app