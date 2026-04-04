from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class ListIssuesRequest(BaseRequest):
    def __init__(self, owner: str, repo: str, state: str = "open"):
        self.owner = owner
        self.repo = repo
        self.state = state


# --- Response ---
class ListIssuesResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[list[dict]] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or []


# --- UseCase ---
class ListIssuesUseCase(BaseUseCase[ListIssuesRequest, ListIssuesResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: ListIssuesRequest) -> ListIssuesResponse:
        issues = self.repo.list_issues(request.owner, request.repo, request.state, per_page=20)
        data = [
            {
                "number": i.number,
                "title": i.title,
                "state": i.state,
                "url": i.html_url,
                "author": i.user_login,
            }
            for i in issues
        ]
        return ListIssuesResponse(success=True, data=data)