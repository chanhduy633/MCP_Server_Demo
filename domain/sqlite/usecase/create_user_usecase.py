from typing import Optional
from domain.sqlite.interface.i_user_repository import IUserRepository
from shared.base import BaseRequest
from shared.base import BaseResponse
from shared.base import BaseUseCase

class CreateUserRequest(BaseRequest):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
 
 
class CreateUserResponse(BaseResponse):
    def __init__(
        self,
        success: bool,
        data: Optional[dict] = None,
        message: str = "",
    ):
        super().__init__(success, message)
        self.data = data or {}
 
 
class CreateUserUseCase(BaseUseCase[CreateUserRequest, CreateUserResponse]):
 
    def __init__(self, repo: IUserRepository):
        self.repo = repo
 
    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        if not request.name.strip():
            return CreateUserResponse(success=False, message="Tên không được để trống")
        if "@" not in request.email:
            return CreateUserResponse(success=False, message="Email không hợp lệ")
 
        user = self.repo.create_user(request.name, request.email)
        return CreateUserResponse(
            success=True,
            data={"id": user.id, "name": user.name, "email": user.email},
            message="User created successfully",
        )
 