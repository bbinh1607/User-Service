from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from flask import current_app
from sqlalchemy import make_url
# Khởi tạo các extension
db = SQLAlchemy()
cors = CORS()

# Danh sách các domain được phép truy cập
ALLOWED_ORIGINS = [
    "http://localhost:1.1.1.3000",
    "http://localhost:4000",
    "http://localhost:3000",
    "http://mywebsite.com",
    "https://anotherwebsite.com"
]

# def create_database():
#     """Chỉ tạo database trong thư mục backend nếu chưa tồn tại"""
#     db_folder = os.path.dirname(DATABASE_PATH)

#     if not os.path.exists(db_folder):
#         os.makedirs(db_folder)

#     if not os.path.exists(DATABASE_PATH):
#         open(DATABASE_PATH, 'a').close()

def create_database():
    """Tạo thư mục và file SQLite nếu chưa có"""
    db_uri = current_app.config['SQLALCHEMY_DATABASE_URI']
    url = make_url(db_uri)

    if url.drivername == 'sqlite':
        db_path = url.database
        db_folder = os.path.dirname(db_path)

        if not os.path.exists(db_folder):
            os.makedirs(db_folder, exist_ok=True)

        if not os.path.exists(db_path):
            open(db_path, 'a').close()
    

            
def init_extensions(app):
    """Khởi tạo tất cả các extensions với Flask app"""
    with app.app_context():  # ✅ Đảm bảo đang ở trong context của app
        create_database()
    
    db.init_app(app)
    
    cors.init_app(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}})







