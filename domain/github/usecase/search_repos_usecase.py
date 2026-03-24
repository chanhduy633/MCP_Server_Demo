import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository
 
 
class SearchReposUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, query: str, per_page: int = 10) -> list[dict]:
        repos = self.repo.search_repositories(query, per_page)
        return [
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
 