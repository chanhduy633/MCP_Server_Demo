from repository.sqlite.user_repository import UserRepository

from domain.sqlite.usecase.get_user_usecase import GetUsersUseCase
from domain.sqlite.usecase.create_user_usecase import CreateUserUseCase


class SqliteContainer:
    def __init__(self):
        repo = UserRepository()

        self.get_users = GetUsersUseCase(repo)
        self.create_user = CreateUserUseCase(repo)