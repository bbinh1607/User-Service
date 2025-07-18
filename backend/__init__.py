from flask import Flask
from backend.extensions import db, create_database, cors
from backend.config import Config
from backend.controller import register_controllers
from backend.utils.converters.uuid_converter import UUIDConverter
from backend.entity import *  
from backend.service.role_service import RoleService

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bắt buộc vào context trước khi gọi current_app
    with app.app_context():
        create_database()     # ✅ Tạo thư mục và file DB nếu chưa có
        db.init_app(app)      # ✅ Khởi tạo db sau khi config & path ổn
        db.create_all()
        RoleService().init_role_table()
        

    # Các extensions không cần app context
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

    app.url_map.converters['uuid'] = UUIDConverter

    register_controllers(app)
    
    return app

