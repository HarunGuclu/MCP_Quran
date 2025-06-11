#!/usr/bin/env python3
"""
Test script for Quran MCP Server API functions
"""

from app import (
    get_available_editions, get_surah_list, get_surah, get_ayah, 
    get_random_ayah, search_quran, get_juz, get_sajda_ayahs
)

def test_api_functions():
    """Test all API functions to ensure they work correctly."""
    
    print("🕌 Testing Quran MCP Server API Functions")
    print("=" * 50)
    
    # Test 1: Get Surah list
    print("\n1. Testing get_surah_list()...")
    surahs = get_surah_list()
    if 'data' in surahs:
        print(f"✅ Success: Found {len(surahs['data'])} Surahs")
        print(f"   First Surah: {surahs['data'][0]['englishName']} ({surahs['data'][0]['name']})")
    else:
        print(f"❌ Error: {surahs}")
    
    # Test 2: Get specific Ayah (Ayat Al-Kursi)
    print("\n2. Testing get_ayah() - Ayat Al-Kursi (2:255)...")
    ayah = get_ayah("2:255", "en.asad")
    if 'data' in ayah:
        print("✅ Success: Retrieved Ayat Al-Kursi")
        print(f"   Text: {ayah['data']['text'][:100]}...")
    else:
        print(f"❌ Error: {ayah}")
    
    # Test 3: Get Al-Fatiha (first Surah)
    print("\n3. Testing get_surah() - Al-Fatiha...")
    surah = get_surah(1, "en.pickthall")
    if 'data' in surah:
        print("✅ Success: Retrieved Al-Fatiha")
        print(f"   Name: {surah['data']['englishName']}")
        print(f"   Verses: {surah['data']['numberOfAyahs']}")
    else:
        print(f"❌ Error: {surah}")
    
    # Test 4: Search functionality
    print("\n4. Testing search_quran() - searching for 'mercy'...")
    search_result = search_quran("mercy", "all", "en")
    if 'data' in search_result:
        print(f"✅ Success: Found {search_result['data']['count']} results for 'mercy'")
        if search_result['data']['matches']:
            first_match = search_result['data']['matches'][0]
            print(f"   First match: Surah {first_match['surah']['number']}:{first_match['numberInSurah']}")
    else:
        print(f"❌ Error: {search_result}")
    
    # Test 5: Get available editions
    print("\n5. Testing get_available_editions() - English text editions...")
    editions = get_available_editions(format_type="text", language="en")
    if 'data' in editions:
        print(f"✅ Success: Found {len(editions['data'])} English text editions")
        print(f"   Example: {editions['data'][0]['name']} ({editions['data'][0]['identifier']})")
    else:
        print(f"❌ Error: {editions}")
    
    # Test 6: Get Sajda verses
    print("\n6. Testing get_sajda_ayahs()...")
    sajda = get_sajda_ayahs("en.asad")
    if 'data' in sajda:
        print(f"✅ Success: Found {len(sajda['data']['ayahs'])} Sajda verses")
        first_sajda = sajda['data']['ayahs'][0]
        print(f"   First Sajda: Surah {first_sajda['surah']['englishName']} ({first_sajda['surah']['number']}:{first_sajda['numberInSurah']})")
    else:
        print(f"❌ Error: {sajda}")
    
    # Test 7: Get random Ayah
    print("\n7. Testing get_random_ayah()...")
    random_ayah = get_random_ayah("en.sahih")
    if 'data' in random_ayah:
        print("✅ Success: Retrieved random Ayah")
        print(f"   Reference: Surah {random_ayah['data']['surah']['number']}:{random_ayah['data']['numberInSurah']}")
        print(f"   Text: {random_ayah['data']['text'][:80]}...")
    else:
        print(f"❌ Error: {random_ayah}")
    
    print("\n" + "=" * 50)
    print("🎉 API Testing Complete!")

if __name__ == "__main__":
    test_api_functions()
