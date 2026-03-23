# MCP Demo Project

## Giới thiệu
Project demo **Model Context Protocol (MCP)** kết nối AI với:
- SQLite
- GitHub

---

# Cấu trúc dự án
```text
mcp_demo/
│
│
│   ├── sql
│   │   │
│   │   ├── app/
│   │   │   └── server.py          # MCP server (SQLite)
│   │   │
│   │   ├── domain/
│   │   │   └── user_service.py
│   │   │
│   │   ├── repository/
│   │   │   └── user_repository.py
│   │   │
│   │   └── models/
│   │       └── user.py
│   │
│   └── github
│       │
│       ├── app/
│       │   └── server.py          # MCP server (GitHub)
│       │
│       ├── domain/
│       │   └── github_service.py
│       │
│       ├── repository/
│       │   └── github_repository.py
│       │
│       └── models/
│          └── models.py
│
├── main_sqlite.py        # entry SQLite MCP
├── main_github.py        # entry GitHub MCP
│
├── pyproject.toml
└── README.md

# Cài đặt
python -m venv venv
venv\Scripts\activate
pip install -e .

# Environment
setx GITHUB_TOKEN "your_token"

# Kết nối Claude Desktop
"mcpServers": {
    "demo": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:8000/mcp"
      ]
    }
  }