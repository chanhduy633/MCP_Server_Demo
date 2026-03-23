from abc import ABC, abstractmethod
from typing import Optional
from src.github.models.models import Repository, Issue, PullRequest


class IGithubRepository(ABC):
    """
    Interface định nghĩa contract cho GitHub data access.
    GithubService chỉ biết interface này — không biết implementation cụ thể.
    """

    # ── Repositories ─────────────────────────────────────────────────────────

    @abstractmethod
    def search_repositories(self, query: str, per_page: int = 10) -> list[Repository]:
        ...

    @abstractmethod
    def get_file_contents(self, owner: str, repo: str, path: str) -> dict | list:
        ...

    # ── Issues ────────────────────────────────────────────────────────────────

    @abstractmethod
    def list_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 20,
    ) -> list[Issue]:
        ...

    @abstractmethod
    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: Optional[str] = None,
    ) -> Issue:
        ...

    @abstractmethod
    def update_issue(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        title: Optional[str] = None,
        body: Optional[str] = None,
        state: Optional[str] = None,
    ) -> Issue:
        ...

    # ── Pull Requests ─────────────────────────────────────────────────────────

    @abstractmethod
    def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 20,
    ) -> list[PullRequest]:
        ...

    @abstractmethod
    def create_pull_request(
        self,
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: Optional[str] = None,
    ) -> PullRequest:
        ...