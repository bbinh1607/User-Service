from functools import wraps
from flask import request, g
from backend.error.business_errors import Unauthorized, TokenExpired, InvalidToken, Forbidden
from backend.utils.jwt_helper.token_utils import decode_token

def authentication(role=None, rank=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if (role is not None and role.lower() == "guest") or (rank == 0):
                return f(*args, **kwargs)
            auth_header = request.headers.get("Authorization", "")
            if not auth_header.startswith("Bearer "):
                raise Unauthorized()
            token = auth_header.replace("Bearer ", "").strip()
            try:
                payload = decode_token(token, type="access")
                g.user_id = payload.get("sub")
                g.role = payload.get("role")
                g.rank = payload.get("rank")
                g.token = token

                # Kiểm tra phân quyền nếu có truyền vào
                if role is not None and g.role.lower() != role.lower():
                    raise Forbidden()
                if rank is not None and int(g.rank) < int(rank):
                    raise Forbidden()

            except TokenExpired:
                raise TokenExpired()
            except InvalidToken:
                raise InvalidToken()

            return f(*args, **kwargs)
        
        wrapper._auth_required = True
        return wrapper
    return decorator
