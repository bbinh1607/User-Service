from flask import request, Blueprint
from backend.utils.response.response_helper import api_response
from backend.service.auth_service import AuthService
from backend.service.user_service import UserService
from backend.middleware.auth.auth_middleware import authentication

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()
user_service = UserService()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = auth_service.login(data)
    return api_response(data=result)


@auth_bp.route("/logout", methods=["POST"])
@authentication()
def logout():
    result = auth_service.logout()
    return api_response(data=result)

@auth_bp.route("/verify-token", methods=["POST"])
@authentication()
def verify_token():
    result = auth_service.verify_token()
    return api_response(data=result)

@auth_bp.route("/refresh-token", methods=["POST"])
def refresh_token():
    data = request.get_json()
    result = auth_service.refresh_token(data)
    return api_response(data=result)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = user_service.create_user(data)
    return api_response(data=result)