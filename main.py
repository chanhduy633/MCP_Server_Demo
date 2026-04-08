import contextlib
import os

from mcp.server.fastmcp import FastMCP
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware  # ← thêm
from dotenv import load_dotenv

from shared.db.database import init_db
from shared.auth import create_auth0_verifier
from app.mcp_sqlite import tools as sqlite_tools
from app.mcp_github import tools as github_tools

load_dotenv()

auth0_domain = os.getenv("AUTH0_DOMAIN")
resource_server_url = os.getenv("RESOURCE_SERVER_URL")

if not auth0_domain:
    raise ValueError("AUTH0_DOMAIN environment variable is required")
if not resource_server_url:
    raise ValueError("RESOURCE_SERVER_URL environment variable is required")

token_verifier = create_auth0_verifier()

mcp = FastMCP(
    "MCP Demo Server",
    stateless_http=True,
    json_response=True,
    token_verifier=token_verifier,
    auth=AuthSettings(
        issuer_url=AnyHttpUrl(f"https://{auth0_domain}/"),
        resource_server_url=AnyHttpUrl(resource_server_url),
        required_scopes=["openid", "profile", "email"],
    ),
)

sqlite_tools.register(mcp)
github_tools.register(mcp)


@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with mcp.session_manager.run():
        yield


app = Starlette(
    routes=[Mount("/", app=mcp.streamable_http_app())],
    lifespan=lifespan,
    middleware=[                                          # ← thêm block này
        Middleware(
            TrustedHostMiddleware,
            allowed_hosts=[
                "mcp-server-demo-nine.vercel.app",
                "localhost",
                "127.0.0.1",
                "*",  # hoặc dùng wildcard cho đơn giản
            ]
        )
    ],
)

if __name__ == "__main__":
    import uvicorn
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)