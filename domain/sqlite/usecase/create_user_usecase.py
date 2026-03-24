from domain.sqlite.interface.i_user_repository import IUserRepository
 
 
class CreateUserUseCase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
 
    def execute(self, name: str, email: str) -> dict:
        if not name.strip():
            raise ValueError("Tên không được để trống")
        if "@" not in email:
            raise ValueError("Email không hợp lệ")
 
        user = self.repo.create_user(name, email)
        return {"message": "User created successfully", "id": user.id, "name": user.name}