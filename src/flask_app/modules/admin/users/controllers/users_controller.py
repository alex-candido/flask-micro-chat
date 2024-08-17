import os

from flask import Blueprint, request, render_template, redirect, url_for, flash, abort

__template_folder = os.path.join(os.path.dirname(__file__), "views")

users_controller = Blueprint("AdminUsersController", __name__, template_folder=__template_folder)

@users_controller.route("/users", methods=["GET", "POST"])
def index():
  return "users index"