from mcp.server.fastmcp import FastMCP
from dependencies.github import GithubContainer

from domain.github.usecase.search_repos_usecase import SearchReposRequest, SearchReposResponse
from domain.github.usecase.get_filecontents_usecase import GetFileContentsRequest, GetFileContentsResponse
from domain.github.usecase.list_issues_usecase import ListIssuesRequest, ListIssuesResponse
from domain.github.usecase.create_issue_usecase import CreateIssueRequest, CreateIssueResponse
from domain.github.usecase.close_issue_usecase import CloseIssueRequest, CloseIssueResponse
from domain.github.usecase.list_pullrequests_usecase import ListPullRequestsRequest, ListPullRequestsResponse
from domain.github.usecase.create_pullrequest_usecase import CreatePullRequestRequest, CreatePullRequestResponse


def register(mcp: FastMCP):
    container = GithubContainer()

    @mcp.tool()
    def search_repositories(query: str, per_page: int = 10) -> SearchReposResponse:
        """Search GitHub repositories by keyword."""
        return container.search_repos.execute(SearchReposRequest(query=query, per_page=per_page))

    @mcp.tool()
    def get_file_contents(owner: str, repo: str, path: str) -> GetFileContentsResponse:
        """Get contents of a file or directory from a GitHub repository."""
        return container.get_file.execute(GetFileContentsRequest(owner=owner, repo=repo, path=path))

    @mcp.tool()
    def list_github_issues(owner: str, repo: str, state: str = "open") -> ListIssuesResponse:
        """List issues in a repository. state: open | closed | all."""
        return container.list_issues.execute(ListIssuesRequest(owner=owner, repo=repo, state=state))

    @mcp.tool()
    def create_github_issue(owner: str, repo: str, title: str, body: str = "") -> CreateIssueResponse:
        """Create a new issue in a repository."""
        return container.create_issue.execute(CreateIssueRequest(owner=owner, repo=repo, title=title, body=body or None))

    @mcp.tool()
    def close_github_issue(owner: str, repo: str, issue_number: int) -> CloseIssueResponse:
        """Close an existing issue."""
        return container.close_issue.execute(CloseIssueRequest(owner=owner, repo=repo, issue_number=issue_number))

    @mcp.tool()
    def list_pull_requests(owner: str, repo: str, state: str = "open") -> ListPullRequestsResponse:
        """List pull requests in a repository. state: open | closed | all."""
        return container.list_prs.execute(ListPullRequestsRequest(owner=owner, repo=repo, state=state))

    @mcp.tool()
    def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = "") -> CreatePullRequestResponse:
        """Create a new pull request. head: source branch, base: target branch."""
        return container.create_pr.execute(CreatePullRequestRequest(owner=owner, repo=repo, title=title, head=head, base=base, body=body or None))