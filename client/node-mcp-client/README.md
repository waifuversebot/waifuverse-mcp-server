# MCP Python Bridge 🐱

See the other README instead

Your MCP config should look something like this, assuming that the MCP server is already running on port 8000
{
    "mcpServers": {
        "waifuverse": {
            "command": "npx",
            "args": [
               "atlantis-mcp",
               "--port",
               "8000"
               ]
         }
    }
  }


To add WaifuVerse to Claude Code, use the command:

claude mcp add waifuverse -- npx atlantis-mcp --port 8000

