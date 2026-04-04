from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class CloseIssueRequest(BaseRequest):
    def __init__(self, owner: str, repo: str, issue_number: int):
        self.owner = owner
        self.repo = repo
        self.issue_number = issue_number


# --- Response ---
class CloseIssueResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[dict] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or {}


# --- UseCase ---
class CloseIssueUseCase(BaseUseCase[CloseIssueRequest, CloseIssueResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: CloseIssueRequest) -> CloseIssueResponse:
        issue = self.repo.update_issue(
            request.owner, request.repo, request.issue_number,
            title=None, body=None, state="closed",
        )
        return CloseIssueResponse(
            success=True,
            data={"number": issue.number, "url": issue.html_url},
            message=f"Issue #{issue.number} closed",
        )