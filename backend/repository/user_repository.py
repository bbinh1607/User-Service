from backend.entity.user_entity import UserEntity
from backend.extensions import db
from backend.utils.handle.hande_exception import handle_exceptions_repository_class

@handle_exceptions_repository_class
class UserRepository:
    def __init__(self):
        self.db = db.session

    def get_user_by_id(self, user_id: str):
        return self.db.query(UserEntity).filter(UserEntity.id == user_id).first()

    def get_user_by_username(self, username: str):
        return self.db.query(UserEntity).filter(UserEntity.username == username).first()

    def create_user(self, user: UserEntity):
        self.db.add(user)
        self.db.commit()
        return user

    def update_user(self, user_id: str, user: UserEntity):
        self.db.query(UserEntity).filter(UserEntity.id == user_id).update(user)
        self.db.commit()
        return self.db.query(UserEntity).filter(UserEntity.id == user_id).first()
    
    def delete_user(self, user_id: str):
        self.db.query(UserEntity).filter(UserEntity.id == user_id).delete()
        self.db.commit()
        return self.db.query(UserEntity).filter(UserEntity.id == user_id).first()
    
    def get_all_user(self):
        return self.db.query(UserEntity).all()
    

    