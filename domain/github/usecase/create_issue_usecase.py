import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository

class CreateIssueUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, owner: str, repo: str, title: str, body: Optional[str] = None) -> dict:
        if not title.strip():
            raise ValueError("Tiêu đề issue không được để trống")
        issue = self.repo.create_issue(owner, repo, title, body)
        return {"message": "Issue created successfully", "number": issue.number, "url": issue.html_url}