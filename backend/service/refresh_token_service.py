from backend.repository.refresh_token_repository import RefreshTokenRepository
from backend.schema.refresh_token_schema.refresh_token_schema import RefreshTokenSchema
from backend.entity.refresh_token_entity import RefreshTokenEntity
import secrets
from datetime import datetime, timedelta
from backend.config import REFRESH_TOKEN_EXPIRES

class RefreshTokenService:
    def __init__(self):
        self.refresh_token_repository = RefreshTokenRepository()

    def create_refresh_token(self, id, refresh_token, exp):
        
        if self.get_refresh_token_by_user_id(id) is not None:
            self.delete_refresh_token_by_user_id(id)
        
        refresh_token_entity = RefreshTokenEntity(
            user_id=id,
            refresh_token=refresh_token,
            expires_at=exp
        )
        refresh_token_entity = self.refresh_token_repository.create_refresh_token(refresh_token_entity)
        return refresh_token_entity.refresh_token
    
    def get_refresh_token(self, token):
        return self.refresh_token_repository.get_refresh_token(token)
    
    def delete_refresh_token_by_user_id(self, id):
        return self.refresh_token_repository.delete_refresh_token_by_user_id(id)
    
    def update_refresh_token(self, id):
        data = RefreshTokenSchema().load(data)
        refresh_token_entity = RefreshTokenEntity(
            user_id=data.user_id,
            refresh_token=data.refresh_token,
            expires_at=data.expires_at
        )
        return self.refresh_token_repository.update_refresh_token(refresh_token_entity)
    
    def get_refresh_token_by_user_id(self, user_id):
        return self.refresh_token_repository.get_refresh_token_by_user_id(user_id)