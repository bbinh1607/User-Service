import os
from dotenv import load_dotenv

# Load file .env trong cùng thư mục (backend/)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Biến môi trường
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
REFRESH_TOKEN_EXPIRES = int(os.getenv("REFRESH_TOKEN_EXPIRES", 7))
ACCESS_TOKEN_EXPIRES = int(os.getenv("ACCESS_TOKEN_EXPIRES", 1))
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Lấy DATABASE_PATH từ .env hoặc default
raw_db_path = os.getenv("DATABASE_PATH", "sqlite:///user.db")

# Nếu là SQLite và không có 4 dấu /, thì đang dùng đường dẫn tương đối → cần chuyển thành tuyệt đối
if raw_db_path.startswith("sqlite:///") and not raw_db_path.startswith("sqlite:////"):
    # Tách phần file name (user.db)
    db_filename = raw_db_path.replace("sqlite:///", "")
    # Tạo path tuyệt đối dựa vào vị trí của file config.py (backend/)
    abs_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), db_filename))
    # Gắn lại vào URI
    DATABASE_PATH = f"sqlite:///{abs_db_path}"
else:
    DATABASE_PATH = raw_db_path

class Config:
    """Cấu hình chung cho Flask app"""
    SQLALCHEMY_DATABASE_URI = DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
