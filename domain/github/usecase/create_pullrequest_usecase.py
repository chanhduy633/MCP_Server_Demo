import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository

class CreatePullRequestUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None) -> dict:
        if head == base:
            raise ValueError(f"head '{head}' và base '{base}' không được trùng nhau")
        pr = self.repo.create_pull_request(owner, repo, title, head, base, body)
        return {"message": "Pull request created successfully", "number": pr.number, "url": pr.html_url}