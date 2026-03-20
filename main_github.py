"""
Entry point cho GitHub MCP Server.

Cách chạy thủ công để test:
    python main_github.py

Claude Desktop config:
    {
        "mcpServers": {
            "github": {
                "command": "D:\\Project\\MCP_Demo\\venv\\Scripts\\python.exe",
                "args": ["D:\\Project\\MCP_Demo\\main_github.py"],
                "cwd": "D:\\Project\\MCP_Demo",
                "env": {
                    "PYTHONPATH": "D:\\Project\\MCP_Demo",
                    "GITHUB_TOKEN": "your_token_here"
                }
            }
        }
    }

Lấy token tại: https://github.com/settings/tokens
Quyền cần thiết: repo (full), issues (read/write)
"""

from src.github.app.server import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")