from flask import request
from backend.utils.response.response_helper import api_response
from backend.service.auth_service import AuthService
from backend.utils.route.smart_blueprint import SmartBlueprint
from backend.middleware.auth.auth_middleware import authentication

auth_bp = SmartBlueprint("auth", __name__)
auth_service = AuthService()

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

