from fastmcp import Client

from Servers.basic_mcp_server import mcp

client = Client(mcp)

async def call_tool():
    async with client:
        result = await client.call_tool("add", {"a": 5, "b": 10})
        print(result)
        return result

