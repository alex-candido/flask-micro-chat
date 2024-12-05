from flask import Flask

from flask_app.__share.resources.constants.routes_constant import admin_prefix
from flask_app.modules.admin.users.controllers.users_controller import users_controller

def admin_users_routes(app: Flask):
      app.register_blueprint(users_controller, url_prefix = admin_prefix)