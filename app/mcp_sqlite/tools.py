from mcp.server.fastmcp import FastMCP
from dependencies.sqlite import SqliteContainer


def register(mcp: FastMCP):
    container = SqliteContainer()

    @mcp.tool()
    def get_all_users() -> list[dict]:
        """Get all users from the SQLite database.

        Returns:
            List of users with their information.
        """
        return container.get_users.execute()

    @mcp.tool()
    def create_new_user(name: str, email: str) -> dict:
        """Create a new user in the SQLite database.

        Args:
            name: Full name of the user.
            email: Email address of the user.

        Returns:
            The created user object.
        """
        return container.create_user.execute(name, email)