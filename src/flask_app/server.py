from flask import Flask
from flask_restx import Api

from flask_app.modules.admin.users.routes.users_routes import admin_users_routes
from flask_app.modules.api.users.routes.users_routes import api_users_routes
from flask_app.__share.config import enviroment

def create_app():
  enviroment.load()
  
  app = Flask(__name__)
  
  v1 = Api(app= app, doc="/api/v1", version=1, prefix="/api/v1")
  
  admin_users_routes(app)
  api_users_routes(v1)

  return app