from abc import ABC, abstractmethod
from domain.sqlite.model.user import User

class IUserRepository(ABC):
    """
    Interface định nghĩa contract cho User data access.
    UserService chỉ biết interface này — không biết implementation cụ thể.
    """

    @abstractmethod
    def get_all_users(self) -> list[User]:
        ...

    @abstractmethod
    def create_user(self, name: str, email: str) -> User:
        ...