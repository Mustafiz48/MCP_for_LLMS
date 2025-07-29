import asyncio
from fastmcp import FastMCP

mcp = FastMCP(
    name="Basic MCP Server",
    instructions="Basic mcp server, call add() to perform addition.",)

@mcp.tool
def add(a:int, b:int) -> int:
    """"Add two numbers together."""
    return a + b

async def run_server():
        await mcp.run_async(
        transport="http",
        host="localhost",
        port=8000,
    ) 
if __name__ == "__main__":
    asyncio.run(run_server())