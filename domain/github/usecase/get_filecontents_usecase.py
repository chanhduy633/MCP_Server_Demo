import base64
from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class GetFileContentsRequest(BaseRequest):
    def __init__(self, owner: str, repo: str, path: str):
        self.owner = owner
        self.repo = repo
        self.path = path


# --- Response ---
class GetFileContentsResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[dict] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or {}


# --- UseCase ---
class GetFileContentsUseCase(BaseUseCase[GetFileContentsRequest, GetFileContentsResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: GetFileContentsRequest) -> GetFileContentsResponse:
        raw = self.repo.get_file_contents(request.owner, request.repo, request.path)

        if isinstance(raw, list):
            data = {
                "type": "directory",
                "items": [{"name": f["name"], "type": f["type"], "path": f["path"]} for f in raw],
            }
        else:
            content = base64.b64decode(raw["content"]).decode("utf-8", errors="replace")
            data = {"type": "file", "path": raw["path"], "size": raw["size"], "content": content}

        return GetFileContentsResponse(success=True, data=data)