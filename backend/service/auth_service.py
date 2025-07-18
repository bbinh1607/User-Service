import hashlib
from backend.repository.user_repository import UserRepository
from backend.schema.auth_schema.auth_login_schema import AuthLoginSchema
from backend.schema.auth_schema.auth_repose import AuthResponse
from backend.utils.handle.hande_exception import handle_exceptions_class
from backend.error.business_errors import UserNotFound, InvalidPassword
from backend.service.refresh_token_service import RefreshTokenService
from backend.utils.jwt_helper.token_utils import generate_token
from backend.utils.jwt_helper.token_utils import verify_token
from flask import g

@handle_exceptions_class
class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.refresh_token_service = RefreshTokenService()

    def login(self, data):
        data = AuthLoginSchema().load(data)
        user = self.user_repository.get_user_by_username(data.username)
        if user is None:
            raise UserNotFound()
        if user.password != hashlib.sha256(data.password.encode()).hexdigest():
            raise InvalidPassword()
        access_token, refresh_token , refresh_token_expires = generate_token(user)
        self.refresh_token_service.create_refresh_token(user.id, refresh_token, refresh_token_expires)
        
        return AuthResponse(
            access_token=access_token,
            refresh_token=refresh_token
        )

    
    def logout(self):
        self.refresh_token_service.delete_refresh_token_by_user_id(g.user_id)
        return True
    
    
    def refresh_token(self, refresh_token):
        pass
    
    def verify_token(self):
        payload = verify_token()
        return payload
    