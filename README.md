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
│   │   │   └── tools.py 
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
│       │   └── tools.py 
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
├── main.py
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
<<<<<<< HEAD
"mcpServers": {
=======
{
  "mcpServers": {
>>>>>>> 4e461e2 (update readme.md)
    "demo": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:8000/mcp"
      ]
    }
  }