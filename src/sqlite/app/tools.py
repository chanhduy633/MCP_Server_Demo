# src/sqlite/app/tools.py
from mcp.server.fastmcp import FastMCP
from src.sqlite.domain.user_service import UserService

def register(mcp: FastMCP):
    service = UserService()

    @mcp.tool()
    def get_users() -> list[dict]:
        """Get all users from the SQLite database."""
        return service.list_users()

    @mcp.tool()
    def create_user(name: str, email: str) -> dict:
        """Create a new user."""
        return service.add_user(name, email)