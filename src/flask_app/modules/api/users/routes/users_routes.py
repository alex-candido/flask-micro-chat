from flask_restx import Api

from flask_app.modules.api.users.controllers.users_controller import UsersController

def api_users_routes(api: Api):
    api.add_resource(UsersController,'/users')