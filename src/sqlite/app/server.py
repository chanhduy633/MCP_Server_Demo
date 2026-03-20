from mcp.server.fastmcp import FastMCP
from src.sqlite.domain.user_service import UserService

mcp = FastMCP("sqlite-mcp-server")
service = UserService()


@mcp.tool()
def get_users():
    """Get all users from database"""
    return service.list_users()


@mcp.tool()
def create_user(name: str, email: str):
    """Create a new user"""
    return service.add_user(name, email)