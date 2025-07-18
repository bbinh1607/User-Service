from backend.repository.user_repository import UserRepository
from backend.entity.user_entity import UserEntity
import hashlib
from backend.service.role_service import RoleService
from backend.utils.handle.hande_exception import handle_exceptions_class
from backend.schema.user_schema.user_create_schema import UserCreateSchema
from backend.schema.user_schema.user_reponse import UserResponseSchema

@handle_exceptions_class
class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.role_service = RoleService()

    def create_user(self, user):
        user = UserCreateSchema().load(user)
        user.password = hashlib.sha256(user.password.encode()).hexdigest()
        if user.role_id is None:
            user.role_id = self.role_service.get_role_by_name("guest").id
        user = self.user_repository.create_user(user)
        return UserResponseSchema().dump(user)
    
    def get_user_by_id(self, user_id: str):
        user = self.user_repository.get_user_by_id(user_id)
        return UserResponseSchema().dump(user)
    
    def get_user_by_username(self, username: str):
        user = self.user_repository.get_user_by_username(username)
        return UserResponseSchema().dump(user)
    
    def get_all_user(self):
        users = self.user_repository.get_all_user()
        return UserResponseSchema().dump(users, many=True)
    
    def update_user(self, user_id: str, user: UserEntity):
        user = UserCreateSchema.load(user)
        user = self.user_repository.update_user(user_id, user)
        return UserResponseSchema().dump(user)
    
    def delete_user(self, user_id: str):
        user = self.user_repository.delete_user(user_id)
        return UserResponseSchema().dump(user)
    
