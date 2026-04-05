from mcp.server.fastmcp import FastMCP
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl
from dotenv import load_dotenv

from shared.db.database import init_db
from shared.auth import create_auth0_verifier
from app.mcp_sqlite import tools as sqlite_tools
from app.mcp_github import tools as github_tools

import os

load_dotenv()

# Validate required env vars early
auth0_domain = os.getenv("AUTH0_DOMAIN")
resource_server_url = os.getenv("RESOURCE_SERVER_URL")

if not auth0_domain:
    raise ValueError("AUTH0_DOMAIN environment variable is required")
if not resource_server_url:
    raise ValueError("RESOURCE_SERVER_URL environment variable is required")

# Initialize Auth0 token verifier
token_verifier = create_auth0_verifier()

mcp = FastMCP(
    "MCP Demo Server",
    host="0.0.0.0",
    token_verifier=token_verifier,
    auth=AuthSettings(
        issuer_url=AnyHttpUrl(f"https://{auth0_domain}/"),
        resource_server_url=AnyHttpUrl(resource_server_url),
        required_scopes=["openid", "profile", "email"],
    ),
)

sqlite_tools.register(mcp)
github_tools.register(mcp)

if __name__ == "__main__":
    init_db()
    mcp.run(transport="streamable-http")