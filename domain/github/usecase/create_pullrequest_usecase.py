from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class CreatePullRequestRequest(BaseRequest):
    def __init__(self, owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None):
        self.owner = owner
        self.repo = repo
        self.title = title
        self.head = head
        self.base = base
        self.body = body


# --- Response ---
class CreatePullRequestResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[dict] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or {}


# --- UseCase ---
class CreatePullRequestUseCase(BaseUseCase[CreatePullRequestRequest, CreatePullRequestResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: CreatePullRequestRequest) -> CreatePullRequestResponse:
        if request.head == request.base:
            return CreatePullRequestResponse(
                success=False,
                message=f"head '{request.head}' và base '{request.base}' không được trùng nhau",
            )

        pr = self.repo.create_pull_request(
            request.owner, request.repo, request.title, request.head, request.base, request.body
        )
        return CreatePullRequestResponse(
            success=True,
            data={"number": pr.number, "url": pr.html_url},
            message="Pull request created successfully",
        )