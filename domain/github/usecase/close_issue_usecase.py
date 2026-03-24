import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository

class CloseIssueUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, owner: str, repo: str, issue_number: int) -> dict:
        issue = self.repo.update_issue(owner, repo, issue_number, title=None, body=None, state="closed")
        return {"message": f"Issue #{issue.number} closed", "url": issue.html_url}