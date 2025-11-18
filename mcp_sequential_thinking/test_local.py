#!/usr/bin/env python3
"""
测试客户端 - 无认证
"""
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def test():
    url = "http://127.0.0.1:8000/mcp"
    print(f"🔌 连接到: {url}")
    print("🔓 无认证模式")
    
    # 不传递任何认证信息
    async with streamablehttp_client(url) as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            # 初始化
            result = await session.initialize()
            print(f"✅ 初始化成功")
            print(f"📝 Session ID: {get_session_id()}")
            print(f"📋 Protocol: {result.protocolVersion}")
            
            # 列出工具
            tools = await session.list_tools()
            print(f"\n📋 找到 {len(tools.tools)} 个工具:")
            for tool in tools.tools:
                print(f"  • {tool.name}")
            
            # 调用工具
            result = await session.call_tool("hello", {"name": "World"})
            print(f"\n✅ 调用结果: {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(test())
