from src.sqlite.interfaces.i_user_repository import IUserRepository

class UserService:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

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