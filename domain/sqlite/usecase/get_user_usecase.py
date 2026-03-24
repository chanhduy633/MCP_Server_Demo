from domain.sqlite.interface.i_user_repository import IUserRepository
 
 
class GetUsersUseCase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
 
    def execute(self) -> list[dict]:
        users = self.repo.get_all_users()
        return [{"id": u.id, "name": u.name, "email": u.email} for u in users]