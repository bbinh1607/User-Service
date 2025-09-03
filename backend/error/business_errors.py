class BusinessError(Exception):
    """Lớp cha cho tất cả các lỗi business logic."""
    status_code = 400  # Mặc định lỗi business là 400 Bad Request

    def __init__(self, message="Business logic error", status_code=None):
        super().__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """Chuyển lỗi thành dict để trả về JSON."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "status_code": self.status_code
        }



class UserAlreadyExists(BusinessError):
    """Lỗi khi tạo user với username đã tồn tại."""
    def __init__(self):
        super().__init__("User already exists", 409)


class UnauthorizedAction(BusinessError):
    """Lỗi khi user không có quyền thực hiện hành động này."""
    def __init__(self):
        super().__init__("You are not authorized to perform this action", 403)

class UserNotFound(BusinessError):
    """Lỗi khi user không tồn tại."""
    def __init__(self):
        super().__init__("User not found", 404)

class InvalidPassword(BusinessError):
    """Lỗi khi mật khẩu không hợp lệ."""
    def __init__(self):
        super().__init__("Invalid password", 401)
        
class TokenExpired(BusinessError):
    """Lỗi khi token hết hạn."""
    def __init__(self):
        super().__init__("Token expired", 401)

class InvalidToken(BusinessError):
    """Lỗi khi token không hợp lệ."""
    def __init__(self):
        super().__init__("Invalid token", 401)
        
class Unauthorized(BusinessError):
    """Lỗi khi user không được phép truy cập."""
    def __init__(self):
        super().__init__("Unauthorized", 401)

class Forbidden(BusinessError):
    """Lỗi khi user không có quyền truy cập."""
    def __init__(self):
        super().__init__("Lỗi khi user không có quyền truy cập", 403)
             
class RefrechTokenNotFount(BusinessError):
    """Lỗi khi user không có quyền truy cập."""
    def __init__(self):
        super().__init__("Không tìm thấy refrech token", 404)
        