from backend.extensions import db
from backend.utils.handle.hande_exception import handle_exceptions_repository_class
from backend.entity.role_entity import RoleEntity

@handle_exceptions_repository_class
class RoleRepository:
    def __init__(self):
        self.db = db.session

    def get_role_by_id(self, role_id: str):
        return self.db.query(RoleEntity).filter(RoleEntity.id == role_id).first()
    
    def get_role_by_name(self, name: str):
        return self.db.query(RoleEntity).filter(RoleEntity.name == name).first()
    
    def get_all_role(self):
        return self.db.query(RoleEntity).all()
    
    def create_role(self, role: RoleEntity):
        self.db.add(role)
        self.db.commit()
        return role
