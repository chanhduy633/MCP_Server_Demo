import os
import requests
from typing import Optional
from src.github.models.models import Repository, Issue, PullRequest


GITHUB_API = "https://api.github.com"


class GithubRepository:
    """
    Repository layer: chỉ làm việc với GitHub REST API.
    Không chứa business logic — chỉ gọi API và map response về model.
    """

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN chưa được set trong environment")

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def _get(self, path: str, params: dict = None) -> dict | list:
        url = f"{GITHUB_API}{path}"
        res = requests.get(url, headers=self.headers, params=params)
        res.raise_for_status()
        return res.json()

    def _post(self, path: str, body: dict) -> dict:
        url = f"{GITHUB_API}{path}"
        res = requests.post(url, headers=self.headers, json=body)
        res.raise_for_status()
        return res.json()

    def _patch(self, path: str, body: dict) -> dict:
        url = f"{GITHUB_API}{path}"
        res = requests.patch(url, headers=self.headers, json=body)
        res.raise_for_status()
        return res.json()

    # ── Repositories ─────────────────────────────────────────────────────────

    def search_repositories(self, query: str, per_page: int = 10) -> list[Repository]:
        data = self._get("/search/repositories", {"q": query, "per_page": per_page})
        return [
            Repository(
                id=r["id"],
                name=r["name"],
                full_name=r["full_name"],
                description=r.get("description"),
                private=r["private"],
                html_url=r["html_url"],
                stargazers_count=r["stargazers_count"],
                language=r.get("language"),
            )
            for r in data["items"]
        ]

    def get_file_contents(self, owner: str, repo: str, path: str) -> dict:
        return self._get(f"/repos/{owner}/{repo}/contents/{path}")

    # ── Issues ────────────────────────────────────────────────────────────────

    def list_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 20,
    ) -> list[Issue]:
        data = self._get(
            f"/repos/{owner}/{repo}/issues",
            {"state": state, "per_page": per_page},
        )
        return [
            Issue(
                number=i["number"],
                title=i["title"],
                body=i.get("body"),
                state=i["state"],
                html_url=i["html_url"],
                user_login=i["user"]["login"],
            )
            for i in data
            if "pull_request" not in i  # lọc bỏ PR ra khỏi issues list
        ]

    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: Optional[str] = None,
    ) -> Issue:
        data = self._post(
            f"/repos/{owner}/{repo}/issues",
            {"title": title, "body": body},
        )
        return Issue(
            number=data["number"],
            title=data["title"],
            body=data.get("body"),
            state=data["state"],
            html_url=data["html_url"],
            user_login=data["user"]["login"],
        )

    def update_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        title: Optional[str] = None,
        body: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Issue:
        payload = {k: v for k, v in {"title": title, "body": body, "state": state}.items() if v is not None}
        data = self._patch(f"/repos/{owner}/{repo}/issues/{issue_number}", payload)
        return Issue(
            number=data["number"],
            title=data["title"],
            body=data.get("body"),
            state=data["state"],
            html_url=data["html_url"],
            user_login=data["user"]["login"],
        )

    # ── Pull Requests ─────────────────────────────────────────────────────────

    def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 20,
    ) -> list[PullRequest]:
        data = self._get(
            f"/repos/{owner}/{repo}/pulls",
            {"state": state, "per_page": per_page},
        )
        return [
            PullRequest(
                number=p["number"],
                title=p["title"],
                body=p.get("body"),
                state=p["state"],
                html_url=p["html_url"],
                head_branch=p["head"]["ref"],
                base_branch=p["base"]["ref"],
                user_login=p["user"]["login"],
            )
            for p in data
        ]

    def create_pull_request(
        self,
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: Optional[str] = None,
    ) -> PullRequest:
        data = self._post(
            f"/repos/{owner}/{repo}/pulls",
            {"title": title, "head": head, "base": base, "body": body},
        )
        return PullRequest(
            number=data["number"],
            title=data["title"],
            body=data.get("body"),
            state=data["state"],
            html_url=data["html_url"],
            head_branch=data["head"]["ref"],
            base_branch=data["base"]["ref"],
            user_login=data["user"]["login"],
        )   