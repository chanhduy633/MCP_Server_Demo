# src/github/app/tools.py
from mcp.server.fastmcp import FastMCP
from src.github.domain.github_service import GithubService

def register(mcp: FastMCP):
    service = GithubService()

    @mcp.tool()
    def search_repositories(query: str, per_page: int = 10) -> list[dict]:
        """
        Search GitHub repositories by keyword.

        Args:
            query: Search keyword (e.g. "fastapi", "react hooks")
            per_page: Number of results to return (default 10, max 100)
        """
        return service.search_repositories(query, per_page)


    @mcp.tool()
    def get_file_contents(owner: str, repo: str, path: str) -> dict:
        """
        Get contents of a file or directory from a GitHub repository.

        Args:
            owner: Repository owner (username or org)
            repo: Repository name
            path: Path to file or directory (e.g. "README.md", "src/")
        """
        return service.get_file_contents(owner, repo, path)


    # ── Issues ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_issues(owner: str, repo: str, state: str = "open") -> list[dict]:
        """
        List issues in a repository.

        Args:
            owner: Repository owner
            repo: Repository name
            state: Filter by state — "open", "closed", or "all"
        """
        return service.list_issues(owner, repo, state)


    @mcp.tool()
    def create_issue(owner: str, repo: str, title: str, body: str = "") -> dict:
        """
        Create a new issue in a repository.

        Args:
            owner: Repository owner
            repo: Repository name
            title: Issue title
            body: Issue description (optional)
        """
        return service.create_issue(owner, repo, title, body or None)


    @mcp.tool()
    def close_issue(owner: str, repo: str, issue_number: int) -> dict:
        """
        Close an existing issue.

        Args:
            owner: Repository owner
            repo: Repository name
            issue_number: Issue number to close
        """
        return service.close_issue(owner, repo, issue_number)


    # ── Pull Requests ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_pull_requests(owner: str, repo: str, state: str = "open") -> list[dict]:
        """
        List pull requests in a repository.

        Args:
            owner: Repository owner
            repo: Repository name
            state: Filter by state — "open", "closed", or "all"
        """
        return service.list_pull_requests(owner, repo, state)


    @mcp.tool()
    def create_pull_request(
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: str = "",
    ) -> dict:
        """
        Create a new pull request.

        Args:
            owner: Repository owner
            repo: Repository name
            title: PR title
            head: Branch with your changes (e.g. "feature/login")
            base: Branch to merge into (e.g. "main")
            body: PR description (optional)
        """
        return service.create_pull_request(owner, repo, title, head, base, body or None)