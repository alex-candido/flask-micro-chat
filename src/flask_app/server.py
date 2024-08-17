from flask import Flask
from flask_restx import Api
from prisma import Prisma, register
from hashids import Hashids

from flask_app.__share.database.prisma.db import PrismaModule

from flask_app.modules.admin.users.routes.users_routes import admin_users_routes
from flask_app.modules.__api.v1.users.routes.users_routes import api_users_routes

def create_app():

  get_db = PrismaModule.get_db
  close_db = PrismaModule.close_db
  
  register(get_db)

  app = Flask(__name__)
  app.teardown_appcontext(close_db)

  hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

  v1 = Api(app= app, doc="/api/v1", version=1, prefix="/api/v1")
  
  admin_users_routes(app)
  api_users_routes(v1)

  return app