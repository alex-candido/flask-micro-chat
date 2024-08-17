from flask_restx import Resource, reqparse

class UsersController(Resource):
    def get(self):
      return "api users"