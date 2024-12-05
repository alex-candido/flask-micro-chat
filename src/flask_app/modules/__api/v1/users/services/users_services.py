from prisma.models import User
from dataclasses import dataclass

@dataclass(kw_only=True, frozen=True, slots=True)
class UserServices:
    
    def create_user(self, data):
        return User.prisma().create(data=data)

    def get_all_users(self):
        return User.prisma().find_many()

    def get_user_by_id(self, user_id):
        return User.prisma().find_unique(where={"id": user_id})

    def update_user(self, user_id, data):
        return User.prisma().update(where={"id": user_id}, data=data)

    def delete_user(self, user_id):
        return User.prisma().delete(where={"id": user_id})