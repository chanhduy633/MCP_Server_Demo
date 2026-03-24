import base64
from typing import Optional
from domain.github.interface.i_github_repository import IGithubRepository

 
class GetFileContentsUseCase:
    def __init__(self, repo: IGithubRepository):
        self.repo = repo
 
    def execute(self, owner: str, repo: str, path: str) -> dict:
        data = self.repo.get_file_contents(owner, repo, path)
 
        if isinstance(data, list):
            return {
                "type": "directory",
                "items": [{"name": f["name"], "type": f["type"], "path": f["path"]} for f in data],
            }
 
        content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        return {"type": "file", "path": data["path"], "size": data["size"], "content": content}
 