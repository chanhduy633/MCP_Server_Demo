from repository.github.github_repository import GithubRepository

from domain.github.usecase.search_repos_usecase import SearchReposUseCase
from domain.github.usecase.get_filecontents_usecase import GetFileContentsUseCase
from domain.github.usecase.list_issues_usecase import ListIssuesUseCase
from domain.github.usecase.create_issue_usecase import CreateIssueUseCase
from domain.github.usecase.close_issue_usecase import CloseIssueUseCase
from domain.github.usecase.list_pullrequests_usecase import ListPullRequestsUseCase
from domain.github.usecase.create_pullrequest_usecase import CreatePullRequestUseCase


class GithubContainer:
    def __init__(self):
        repo = GithubRepository()

        self.search_repos = SearchReposUseCase(repo)
        self.get_file = GetFileContentsUseCase(repo)
        self.list_issues = ListIssuesUseCase(repo)
        self.create_issue = CreateIssueUseCase(repo)
        self.close_issue = CloseIssueUseCase(repo)
        self.list_prs = ListPullRequestsUseCase(repo)
        self.create_pr = CreatePullRequestUseCase(repo)