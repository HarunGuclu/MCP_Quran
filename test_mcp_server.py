#!/usr/bin/env python3
"""
Test script for Quran MCP Server
"""

import asyncio
import json
from server import QuranMCPServer

async def test_mcp_server():
    """Test the MCP server functionality"""
    
    print("🕌 Testing Quran MCP Server")
    print("=" * 40)
    
    server = QuranMCPServer()
    
    # Test 1: List tools
    print("\n1. Testing tools/list...")
    request = {"method": "tools/list"}
    response = await server.handle_request(request)
    
    if "tools" in response:
        print(f"✅ Success: Found {len(response['tools'])} tools")
        for tool in response['tools'][:3]:  # Show first 3 tools
            print(f"   - {tool['name']}: {tool['description']}")
    else:
        print(f"❌ Error: {response}")
    
    # Test 2: Get random Ayah
    print("\n2. Testing get_random_quran_ayah...")
    request = {
        "method": "tools/call",
        "params": {
            "name": "get_random_quran_ayah",
            "arguments": {"edition": "en.asad"}
        }
    }
    response = await server.handle_request(request)
    
    if "content" in response:
        print("✅ Success: Retrieved random Ayah")
        # Parse the JSON content
        content = json.loads(response['content'][0]['text'])
        if 'data' in content:
            ayah_data = content['data']
            print(f"   Reference: Surah {ayah_data['surah']['number']}:{ayah_data['numberInSurah']}")
            print(f"   Text: {ayah_data['text'][:80]}...")
    else:
        print(f"❌ Error: {response}")
    
    # Test 3: Get specific Ayah (Ayat Al-Kursi)
    print("\n3. Testing get_quran_ayah - Ayat Al-Kursi...")
    request = {
        "method": "tools/call",
        "params": {
            "name": "get_quran_ayah",
            "arguments": {
                "reference": "2:255",
                "edition": "en.pickthall"
            }
        }
    }
    response = await server.handle_request(request)
    
    if "content" in response:
        print("✅ Success: Retrieved Ayat Al-Kursi")
        content = json.loads(response['content'][0]['text'])
        if 'data' in content:
            print(f"   Text: {content['data']['text'][:100]}...")
    else:
        print(f"❌ Error: {response}")
    
    # Test 4: List Surahs
    print("\n4. Testing list_quran_surahs...")
    request = {
        "method": "tools/call",
        "params": {
            "name": "list_quran_surahs",
            "arguments": {}
        }
    }
    response = await server.handle_request(request)
    
    if "content" in response:
        print("✅ Success: Retrieved Surah list")
        content = json.loads(response['content'][0]['text'])
        if 'data' in content:
            print(f"   Total Surahs: {len(content['data'])}")
            print(f"   First Surah: {content['data'][0]['englishName']}")
    else:
        print(f"❌ Error: {response}")
    
    # Test 5: Search functionality
    print("\n5. Testing search_quran_text...")
    request = {
        "method": "tools/call",
        "params": {
            "name": "search_quran_text",
            "arguments": {
                "keyword": "peace",
                "edition": "en"
            }
        }
    }
    response = await server.handle_request(request)
    
    if "content" in response:
        print("✅ Success: Search completed")
        content = json.loads(response['content'][0]['text'])
        if 'data' in content:
            print(f"   Found {content['data']['count']} results for 'peace'")
    else:
        print(f"❌ Error: {response}")
    
    print("\n" + "=" * 40)
    print("🎉 MCP Server Testing Complete!")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
