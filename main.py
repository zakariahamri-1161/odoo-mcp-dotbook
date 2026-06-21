"""Alpic entry point — stdio; Alpic wraps it as HTTP."""

from mcp_server_odoo.server import OdooMCPServer

server = OdooMCPServer()
mcp = server.app

if __name__ == "__main__":
    mcp.run(transport="stdio")
