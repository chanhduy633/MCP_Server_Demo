from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
 
Req = TypeVar("Req")
Res = TypeVar("Res")
 
 
class BaseRequest:
    """Mọi request đều kế thừa class này."""
    pass
 
 
class BaseResponse:
    """
    Mọi response đều kế thừa class này.
    - success: thành công hay không
    - message: thông báo lỗi hoặc mô tả
    """
    def __init__(self, success: bool, message: str = ""):
        self.success = success
        self.message = message
 
 
class BaseUseCase(ABC, Generic[Req, Res]):
    """
    Contract chung cho tất cả UseCase trong hệ thống.
    - Req: kiểu request đầu vào (phải kế thừa BaseRequest)
    - Res: kiểu response đầu ra (phải kế thừa BaseResponse)
 
    Lưu ý: dùng sync vì SQLite không cần async.
    """
 
    @abstractmethod
    def execute(self, request: Req) -> Res:
        pass
 
 