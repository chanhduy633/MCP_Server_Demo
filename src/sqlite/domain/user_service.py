from src.sqlite.repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def list_users(self):
        users = self.repo.get_all_users()

        return [
            {
                "id": u.id,
                "name": u.name,
                "email": u.email
            }
            for u in users
        ]

    def add_user(self, name, email):
        self.repo.create_user(name, email)
        return {"message": "User created successfully"}