import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository


class ListPullRequestsUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, owner: str, repo: str, state: str = "open") -> list[dict]:
        prs = self.repo.list_pull_requests(owner, repo, state, per_page=20)
        return [
            {"number": p.number, "title": p.title, "state": p.state,
             "from": p.head_branch, "into": p.base_branch, "url": p.html_url, "author": p.user_login}
            for p in prs
        ]