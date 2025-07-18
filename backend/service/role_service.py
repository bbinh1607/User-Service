from backend.repository.role_reponsitory import RoleRepository
from backend.entity.role_entity import RoleEntity
from datetime import datetime
from uuid import uuid4

class RoleService:
    def __init__(self):
        self.role_repository = RoleRepository()

    def create_role(self, role: RoleEntity):
        return self.role_repository.create_role(role)

    def get_role_by_name(self, name: str):
        role = self.role_repository.get_role_by_name(name)
        return role

    def init_role_table(self):
        """Khởi tạo role table chỉ nếu chưa có dữ liệu"""
        # Kiểm tra xem đã có role nào chưa
        existing_role = self.get_role_by_name("admin")
        if existing_role:
            return

        now = datetime.utcnow()

        roles = [
            RoleEntity(
                id=str(uuid4()),
                name="admin",
                description="Full access to the system",
                rank=4,
                created_at=now,
                updated_at=now
            ),
            RoleEntity(
                id=str(uuid4()),
                name="employee",
                description="Internal staff with general access",
                rank=3,
                created_at=now,
                updated_at=now
            ),
            RoleEntity(
                id=str(uuid4()),
                name="technician",
                description="Handles technical operations and maintenance",
                rank=2,
                created_at=now,
                updated_at=now
            ),
            RoleEntity(
                id=str(uuid4()),
                name="user",
                description="Regular user with basic access",
                rank=1,
                created_at=now,
                updated_at=now
            ),
            RoleEntity(
                id=str(uuid4()),
                name="guest",
                description="Limited access to public content only",
                rank=0,
                created_at=now,
                updated_at=now
            )
        ]

        for role in roles:
            self.create_role(role)
