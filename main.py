# main.py
from mcp.server.fastmcp import FastMCP
from src.sqlite.db.database import init_db
from src.sqlite.app import tools as sqlite_tools
from src.github.app import tools as github_tools

mcp = FastMCP("MCP Demo Server")

# Đăng ký tools từ tất cả domain vào 1 server
sqlite_tools.register(mcp)
github_tools.register(mcp)

if __name__ == "__main__":
    init_db()
    mcp.run(transport="streamable-http")  # HTTP thay vì stdio