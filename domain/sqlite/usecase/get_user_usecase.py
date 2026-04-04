from typing import Optional
from domain.sqlite.interface.i_user_repository import IUserRepository
from shared.base import BaseRequest
from shared.base import BaseResponse
from shared.base import BaseUseCase

 
 
class GetUsersRequest(BaseRequest):
    """Không cần tham số — lấy toàn bộ users."""
    pass
 
class GetUsersResponse(BaseResponse):
    def __init__(
        self,
        success: bool,
        data: Optional[list[dict]] = None,
        message: str = "",
    ):
        super().__init__(success, message)
        self.data = data or []
 
 
class GetUsersUseCase(BaseUseCase[GetUsersRequest, GetUsersResponse]):
 
    def __init__(self, repo: IUserRepository):
        self.repo = repo
 
    def execute(self, request: GetUsersRequest) -> GetUsersResponse:
        users = self.repo.get_all_users()
        data = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
        return GetUsersResponse(success=True, data=data)
 