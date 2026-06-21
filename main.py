"""Alpic entry point for the Odoo MCP server."""

from mcp_server_odoo.server import OdooMCPServer

server = OdooMCPServer()
mcp = server.app

# Alpic's gateway and validation use stateless streamable-http.
mcp.settings.stateless_http = True

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
