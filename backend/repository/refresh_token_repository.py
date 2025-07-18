from backend.extensions import db
from backend.utils.handle.hande_exception import handle_exceptions_repository_class
from backend.entity.refresh_token_entity import RefreshTokenEntity

@handle_exceptions_repository_class
class RefreshTokenRepository:
    def __init__(self):
        self.db = db.session

    def create_refresh_token(self, refresh_token_entity):
        self.db.add(refresh_token_entity)
        self.db.commit()
        return refresh_token_entity
    
    def get_refresh_token(self, token):
        return self.db.query(RefreshTokenEntity).filter(RefreshTokenEntity.token == token).first()
    
    def delete_refresh_token_by_user_id(self, id):
        self.db.query(RefreshTokenEntity).filter(RefreshTokenEntity.user_id == id).delete()
        self.db.commit()
        return self.db.query(RefreshTokenEntity).filter(RefreshTokenEntity.user_id == id).first()
    
    def update_refresh_token(self, refresh_token_entity):
        self.db.query(RefreshTokenEntity).filter(RefreshTokenEntity.id == refresh_token_entity.id).update(refresh_token_entity)
        self.db.commit()
        return self.db.query(RefreshTokenEntity).filter(RefreshTokenEntity.id == refresh_token_entity.id).first()
    
    def get_refresh_token_by_user_id(self, user_id):
        return self.db.query(RefreshTokenEntity).filter(RefreshTokenEntity.user_id == user_id).first()
    