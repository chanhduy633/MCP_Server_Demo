from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class ListPullRequestsRequest(BaseRequest):
    def __init__(self, owner: str, repo: str, state: str = "open"):
        self.owner = owner
        self.repo = repo
        self.state = state


# --- Response ---
class ListPullRequestsResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[list[dict]] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or []


# --- UseCase ---
class ListPullRequestsUseCase(BaseUseCase[ListPullRequestsRequest, ListPullRequestsResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: ListPullRequestsRequest) -> ListPullRequestsResponse:
        prs = self.repo.list_pull_requests(request.owner, request.repo, request.state, per_page=20)
        data = [
            {
                "number": p.number,
                "title": p.title,
                "state": p.state,
                "from": p.head_branch,
                "into": p.base_branch,
                "url": p.html_url,
                "author": p.user_login,
            }
            for p in prs
        ]
        return ListPullRequestsResponse(success=True, data=data)