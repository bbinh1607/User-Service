from backend.service.user_service import UserService
from flask import request
from backend.utils.response.response_helper import api_response
from backend.middleware.auth.auth_middleware import authentication
from backend.utils.route.smart_blueprint import SmartBlueprint

user_bp = SmartBlueprint("user", __name__)
user_service = UserService()

@user_bp.route("/create", methods=["POST"])
@authentication(rank=0)
def create_user():
    data = request.get_json()
    result = user_service.create_user(data)
    return api_response(data=result)

@user_bp.route("/get-all", methods=["GET"])
@authentication(rank=3)
def get_all_user():
    result = user_service.get_all_user()
    return api_response(data=result)

@user_bp.route("/<id>", methods=["GET"])
def get_user_by_id(id):
    result = user_service.get_user_by_id(id)
    return api_response(data=result)

@user_bp.route("/<id>", methods=["DELETE"])
def delete_user_by_id(id):
    result = user_service.delete_user(id)
    return api_response(data=result)

@user_bp.route("/<id>", methods=["PUT"])
def update_user_by_id(id):
    data = request.get_json()
    result = user_service.update_user(id, data)
    return api_response(data=result)

