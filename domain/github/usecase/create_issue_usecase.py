from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class CreateIssueRequest(BaseRequest):
    def __init__(self, owner: str, repo: str, title: str, body: Optional[str] = None):
        self.owner = owner
        self.repo = repo
        self.title = title
        self.body = body


# --- Response ---
class CreateIssueResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[dict] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or {}


# --- UseCase ---
class CreateIssueUseCase(BaseUseCase[CreateIssueRequest, CreateIssueResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: CreateIssueRequest) -> CreateIssueResponse:
        if not request.title.strip():
            return CreateIssueResponse(success=False, message="Tiêu đề issue không được để trống")

        issue = self.repo.create_issue(request.owner, request.repo, request.title, request.body)
        return CreateIssueResponse(
            success=True,
            data={"number": issue.number, "url": issue.html_url},
            message="Issue created successfully",
        )