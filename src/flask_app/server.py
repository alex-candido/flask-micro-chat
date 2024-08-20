import os

from typing import Optional
from flask import Flask, g
from flask_restx import Api
from prisma import Prisma, register, get_client
from flask_debugtoolbar import DebugToolbarExtension

from flask_app.__share.database.prisma.db import PrismaModule

from flask_app.modules.admin.users.routes.users_routes import admin_users_routes
from flask_app.modules.__api.v1.users.routes.users_routes import api_users_routes

def create_app():

    get_db = PrismaModule.get_db
    close_db = PrismaModule.close_db
    
    register(get_db)

    app = Flask(__name__)
    app.teardown_appcontext(close_db)
    
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    toolbar = DebugToolbarExtension(app)

    api_users_routes(app)  
    admin_users_routes(app)

    return app