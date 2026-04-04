import base64
from typing import Optional
from shared.base import BaseRequest, BaseResponse, BaseUseCase
from domain.github.interface.i_github_repository import IGithubRepository


# --- Request ---
class SearchReposRequest(BaseRequest):
    def __init__(self, query: str, per_page: int = 10):
        self.query = query
        self.per_page = per_page


# --- Response ---
class SearchReposResponse(BaseResponse):
    def __init__(self, success: bool, data: Optional[list[dict]] = None, message: str = ""):
        super().__init__(success, message)
        self.data = data or []


# --- UseCase ---
class SearchReposUseCase(BaseUseCase[SearchReposRequest, SearchReposResponse]):
    def __init__(self, repo: IGithubRepository):
        self.repo = repo

    def execute(self, request: SearchReposRequest) -> SearchReposResponse:
        repos = self.repo.search_repositories(request.query, request.per_page)
        data = [
            {
                "name": r.full_name,
                "description": r.description or "(no description)",
                "private": r.private,
                "url": r.html_url,
                "stars": r.stargazers_count,
                "language": r.language or "unknown",
            }
            for r in repos
        ]
        return SearchReposResponse(success=True, data=data)