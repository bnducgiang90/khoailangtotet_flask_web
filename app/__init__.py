import sys

sys.path.append('.')  # đoạn này để gọi import root folder của project vào module này : để gọi được đến các folder khác
from flask import Flask
from app.controllers import main, errors
from app.controllers.Users import usercontroller

# import extensions
# import config

blueprints = (main, errors, usercontroller.bp_user)


def create_app():
    app = Flask(__name__, template_folder='views')
    # app.config.from_object(config.ConfigObject)
    init_blueprints(app)
    init_extensions(app)
    init_other(app)
    return app


def init_blueprints(app):
    for bp in blueprints:
        app.register_blueprint(bp)


def init_extensions(app):
    pass


def init_other(app):
    pass
