from typing import Optional
from src.github.repository.github_repository import GithubRepository


class GithubService:
    """
    Domain layer: chứa business logic.
    Nhận dữ liệu từ Repository, xử lý rồi trả về dict sạch cho App layer.
    """

    def __init__(self):
        self.repo = GithubRepository()

    # ── Repositories ─────────────────────────────────────────────────────────

    def search_repositories(self, query: str, per_page: int = 10) -> list[dict]:
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

    def get_file_contents(self, owner: str, repo: str, path: str) -> dict:
        data = self.repo.get_file_contents(owner, repo, path)

        # Nếu là directory thì trả về danh sách file
        if isinstance(data, list):
            return {
                "type": "directory",
                "items": [{"name": f["name"], "type": f["type"], "path": f["path"]} for f in data],
            }

        # Nếu là file thì decode content
        import base64
        content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        return {
            "type": "file",
            "path": data["path"],
            "size": data["size"],
            "content": content,
        }

    # ── Issues ────────────────────────────────────────────────────────────────

    def list_issues(self, owner: str, repo: str, state: str = "open") -> list[dict]:
        issues = self.repo.list_issues(owner, repo, state)
        return [
            {
                "number": i.number,
                "title": i.title,
                "state": i.state,
                "url": i.html_url,
                "author": i.user_login,
            }
            for i in issues
        ]

    def create_issue(self, owner: str, repo: str, title: str, body: Optional[str] = None) -> dict:
        if not title.strip():
            raise ValueError("Tiêu đề issue không được để trống")

        issue = self.repo.create_issue(owner, repo, title, body)
        return {
            "message": "Issue created successfully",
            "number": issue.number,
            "url": issue.html_url,
        }

    def close_issue(self, owner: str, repo: str, issue_number: int) -> dict:
        issue = self.repo.update_issue(owner, repo, issue_number, state="closed")
        return {
            "message": f"Issue #{issue.number} closed",
            "url": issue.html_url,
        }

    # ── Pull Requests ─────────────────────────────────────────────────────────

    def list_pull_requests(self, owner: str, repo: str, state: str = "open") -> list[dict]:
        prs = self.repo.list_pull_requests(owner, repo, state)
        return [
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

    def create_pull_request(
        self,
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: Optional[str] = None,
    ) -> dict:
        if head == base:
            raise ValueError(f"head branch '{head}' và base branch '{base}' không được trùng nhau")

        pr = self.repo.create_pull_request(owner, repo, title, head, base, body)
        return {
            "message": "Pull request created successfully",
            "number": pr.number,
            "url": pr.html_url,
        }