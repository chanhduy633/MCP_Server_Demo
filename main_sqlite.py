from src.sqlite.app.server import mcp
from src.sqlite.db.database import init_db

def main():
    # Initialize and run the server
    mcp.run(transport="stdio")

if __name__ == "__main__":
    # print("Starting MCP server...")
    init_db()
    main()