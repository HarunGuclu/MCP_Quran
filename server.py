"""
Quran MCP Server - A Model Context Protocol server for accessing the Holy Quran
Optimized for deployment on Smithery.ai
"""

import asyncio
import json
import sys
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP
from app import (
    get_editions, get_editions_min, get_full_quran,
    get_chapter, get_verse, get_juz, get_ruku, get_page,
    get_manzil, get_maqra, get_quran_info, get_fonts
)

# Initialize MCP server
mcp = FastMCP("quran-mcp")

@mcp.tool()
async def get_quran_editions() -> dict:
    """
    Mevcut tüm Kuran sürümlerini güzelleştirilmiş JSON biçiminde listeler.
    Lists all available Quran editions in pretty JSON format.
    """
    result = get_editions()
    return result

@mcp.tool()
async def get_quran_editions_min() -> dict:
    """
    Mevcut tüm Kuran sürümlerinin küçültülmüş versiyonunu getirir.
    Lists all available Quran editions in minified JSON format.
    """
    result = get_editions_min()
    return result

@mcp.tool()
async def get_quran_full(edition_name: str, script_type: str = "") -> dict:
    """
    Tüm Kuran'ı/Kuran tercümesini getirir.
    Gets the full Quran or translation.

    Args / Parametreler:
        edition_name: Sürüm adı (örn: "ben-muhiuddinkhan") / Edition name (e.g. "ben-muhiuddinkhan")
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_full_quran(edition_name, script_type)
    return result

@mcp.tool()
async def get_quran_chapter(edition_name: str, chapter_no: int, script_type: str = "", minified: bool = False) -> dict:
    """
    Belirtilen bölümün tamamını getirir.
    Gets the full chapter (surah).

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        chapter_no: Bölüm numarası (1-114) / Chapter number (1-114)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
        minified: Küçültülmüş format isteniyor mu / Whether minified format is requested
    """
    result = get_chapter(edition_name, chapter_no, script_type, minified)
    return result

@mcp.tool()
async def get_quran_verse(edition_name: str, chapter_no: int, verse_no: int, script_type: str = "") -> dict:
    """
    Belirtilen ayeti getirir.
    Gets the specified verse.

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        chapter_no: Bölüm numarası (1-114) / Chapter number (1-114)
        verse_no: Ayet numarası / Verse number
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_verse(edition_name, chapter_no, verse_no, script_type)
    return result

@mcp.tool()
async def get_quran_juz(edition_name: str, juz_no: int, script_type: str = "") -> dict:
    """
    Belirtilen cüzü getirir.
    Gets the specified juz.

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        juz_no: Cüz numarası (1-30) / Juz number (1-30)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_juz(edition_name, juz_no, script_type)
    return result

@mcp.tool()
async def get_quran_ruku(edition_name: str, ruku_no: int, script_type: str = "") -> dict:
    """
    Belirtilen rükuyu getirir.
    Gets the specified ruku.

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        ruku_no: Rüku numarası / Ruku number
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_ruku(edition_name, ruku_no, script_type)
    return result

@mcp.tool()
async def get_quran_page(edition_name: str, page_no: int, script_type: str = "") -> dict:
    """
    Belirtilen sayfayı getirir.
    Gets the specified page.

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        page_no: Sayfa numarası / Page number
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_page(edition_name, page_no, script_type)
    return result

@mcp.tool()
async def get_quran_manzil(edition_name: str, manzil_no: int, script_type: str = "") -> dict:
    """
    Belirtilen menzili getirir.
    Gets the specified manzil.

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        manzil_no: Menzil numarası (1-7) / Manzil number (1-7)
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_manzil(edition_name, manzil_no, script_type)
    return result

@mcp.tool()
async def get_quran_maqra(edition_name: str, maqra_no: int, script_type: str = "") -> dict:
    """
    Belirtilen makrayı getirir.
    Gets the specified maqra.

    Args / Parametreler:
        edition_name: Sürüm adı / Edition name
        maqra_no: Makra numarası / Maqra number
        script_type: Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
    """
    result = get_maqra(edition_name, maqra_no, script_type)
    return result

@mcp.tool()
async def get_quran_info() -> dict:
    """
    Kuran'daki cüz sayısı, secdeler, rükular vb. gibi Kuran hakkında tüm ayrıntıları getirir.
    Gets all details about the Quran such as number of juz, sajdas, rukus, etc.
    """
    result = get_quran_info()
    return result

@mcp.tool()
async def get_quran_fonts() -> dict:
    """
    Mevcut Arapça yazı tiplerini listeler.
    Lists available Arabic fonts.
    """
    result = get_fonts()
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")