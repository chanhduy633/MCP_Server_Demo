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
├── app/               
│   ├── mcp_sqlite/
│   │   └── tools.py
│   │
│   └── mcp_github/
│       └── tools.py
│
├── domain/                
│   │
│   ├── sqlite/
│   │   ├── model/
│   │   │   └── user.py
│   │   │
│   │   ├── usecase/
│   │   │   └── get_users.py
│   │   │
│   │   └── interface/
│   │       └── i_user_repository.py
│   │
│   └── github/
│       ├── model/
│       │   └── repo.py
│       │
│       ├── usecase/
│       │   └── get_repos.py
│       │
│       └── interface/
│           └── i_github_repository.py
│
├── repository/            
│   │
│   ├── sqlite/
│   │   └── user_repository.py
│   │
│   └── github/
│       └── github_repository.py
│
├── shared/            
│   │
│   └── db/
│       └── database.py
│
├── dependencies/
│   └── github.py
├── main.py
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