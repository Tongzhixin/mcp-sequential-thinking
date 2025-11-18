#!/usr/bin/env python3
"""
测试 FastMCP 的传输能力
"""
import inspect
from mcp.server.fastmcp import FastMCP

# 创建一个测试 MCP 实例
test_mcp = FastMCP("test")

print("="*60)
print("📦 FastMCP 对象分析")
print("="*60)

# 查看所有公开方法
print("\n🔧 可用方法:")
for name, method in inspect.getmembers(test_mcp, predicate=inspect.ismethod):
    if not name.startswith('_'):
        sig = inspect.signature(method)
        print(f"   • {name}{sig}")

# 查看 run 方法的签名
print("\n🚀 run() 方法详情:")
run_sig = inspect.signature(test_mcp.run)
print(f"   签名: run{run_sig}")
print(f"   文档: {test_mcp.run.__doc__}")

# 检查是否有 get_asgi_app 方法
print("\n🌐 ASGI/HTTP 支持:")
if hasattr(test_mcp, 'get_asgi_app'):
    print("   ✅ 支持 get_asgi_app()")
elif hasattr(test_mcp, 'app'):
    print("   ✅ 有 app 属性")
    print(f"      类型: {type(test_mcp.app)}")
else:
    print("   ⚠️  可能只支持 stdio")

print("\n" + "="*60)

# 查看 FastMCP 类的源码位置
import mcp.server.fastmcp
print(f"\n📁 FastMCP 源码: {mcp.server.fastmcp.__file__}")
print("\n💡 建议:")
print("   1. 查看 run() 方法是否接受 transport 参数")
print("   2. 检查是否有 get_asgi_app() 或类似方法")
print("   3. 如果都不支持，可能需要用 uvicorn 直接运行模块")
