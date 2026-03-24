import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository

class ListIssuesUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, owner: str, repo: str, state: str = "open") -> list[dict]:
        issues = self.repo.list_issues(owner, repo, state, per_page=20)
        return [
            {"number": i.number, "title": i.title, "state": i.state, "url": i.html_url, "author": i.user_login}
            for i in issues
        ]