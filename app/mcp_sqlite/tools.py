from mcp.server.fastmcp import FastMCP
from dependencies.sqlite import SqliteContainer
from domain.sqlite.usecase.get_user_usecase import GetUsersRequest, GetUsersResponse
from domain.sqlite.usecase.create_user_usecase import CreateUserRequest, CreateUserResponse


def register(mcp: FastMCP):
    container = SqliteContainer()

    @mcp.tool()
    def get_all_users() -> GetUsersResponse:
        """Get all users from the SQLite database.

        Returns:
            GetUsersResponse with success status and list of users.
        """
        return container.get_users.execute(GetUsersRequest())

    @mcp.tool()
    def create_new_user(name: str, email: str) -> CreateUserResponse:
        """Create a new user in the SQLite database.

        Args:
            name: Full name of the user.
            email: Email address of the user.

        Returns:
            CreateUserResponse with success status and created user.
        """
        return container.create_user.execute(CreateUserRequest(name=name, email=email))