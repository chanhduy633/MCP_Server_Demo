from dataclasses import dataclass
from typing import Optional


@dataclass
class Repository:
    id: int
    name: str
    full_name: str
    description: Optional[str]
    private: bool
    html_url: str
    stargazers_count: int
    language: Optional[str]


@dataclass
class Issue:
    number: int
    title: str
    body: Optional[str]
    state: str
    html_url: str
    user_login: str


@dataclass
class PullRequest:
    number: int
    title: str
    body: Optional[str]
    state: str
    html_url: str
    head_branch: str
    base_branch: str
    user_login: str