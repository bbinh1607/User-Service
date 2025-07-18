from flask import Blueprint, render_template
from backend.error.error_handlers import error_bp
from backend.controller.user_controller import user_bp
from backend.controller.auth_controller import auth_bp

main_bp = Blueprint("main", __name__)

main_bp.register_blueprint(error_bp, url_prefix="/errors")
main_bp.register_blueprint(user_bp, url_prefix="/users")
main_bp.register_blueprint(auth_bp, url_prefix="/auth")

def register_controllers(app):
    app.register_blueprint(main_bp)

