from flask import Flask

from flask_app.__share.resources.constants.routes_constant import api_prefix
from flask_app.modules.__api.v1.users.controllers.users_controller import users_controller

def api_users_routes(app: Flask):
      app.register_blueprint(users_controller, url_prefix = api_prefix)
