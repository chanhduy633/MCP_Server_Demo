from mcp.server.fastmcp import FastMCP
from dependencies.github import GithubContainer


def register(mcp: FastMCP):
    container = GithubContainer()

    @mcp.tool()
    def search_repositories(query: str, per_page: int = 10):
        """Search GitHub repositories by keyword."""
        return container.search_repos.execute(query, per_page)

    @mcp.tool()
    def get_file_contents(owner: str, repo: str, path: str):
        """Get contents of a file or directory from a GitHub repository."""
        return container.get_file.execute(owner, repo, path)

    @mcp.tool()
    def list_github_issues(owner: str, repo: str, state: str = "open"):
        """List issues in a repository. state: open | closed | all."""
        return container.list_issues.execute(owner, repo, state)

    @mcp.tool()
    def create_github_issue(owner: str, repo: str, title: str, body: str = ""):
        """Create a new issue in a repository."""
        return container.create_issue.execute(owner, repo, title, body or None)

    @mcp.tool()
    def close_github_issue(owner: str, repo: str, issue_number: int):
        """Close an existing issue."""
        return container.close_issue.execute(owner, repo, issue_number)

    @mcp.tool()
    def list_pull_requests(owner: str, repo: str, state: str = "open"):
        """List pull requests in a repository. state: open | closed | all."""
        return container.list_prs.execute(owner, repo, state)

    @mcp.tool()
    def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = ""):
        """Create a new pull request. head: source branch, base: target branch."""
        return container.create_pr.execute(owner, repo, title, head, base, body or None)