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
    get_available_editions, get_surah_list, get_surah, get_ayah,
    get_random_ayah, search_quran, get_juz, get_sajda_ayahs, get_multiple_editions
)

mcp = FastMCP("quran-mcp")

@mcp.tool()
async def list_quran_editions(format_type: str = None, language: str = None, edition_type: str = None) -> dict:
    """
    Get list of all available Quran editions.
    """
    return get_available_editions(format_type, language, edition_type)

@mcp.tool()
async def list_quran_surahs() -> dict:
    """
    Get list of all Surahs in the Quran.
    """
    return get_surah_list()

@mcp.tool()
async def get_quran_surah(surah_number: int, edition: str = "quran-uthmani") -> dict:
    """
    Get a complete Surah from the Quran.
    """
    return get_surah(surah_number, edition)

@mcp.tool()
async def get_quran_ayah(reference: str, edition: str = "quran-uthmani") -> dict:
    """
    Get a specific Ayah (verse) from the Quran.
    """
    return get_ayah(reference, edition)

@mcp.tool()
async def get_random_quran_ayah(edition: str = "quran-uthmani") -> dict:
    """
    Get a random Ayah (verse) from the Quran.
    """
    return get_random_ayah(edition)

@mcp.tool()
async def search_quran_text(keyword: str, surah: str = "all", edition: str = "en") -> dict:
    """
    Search for a keyword in the Quran text.
    """
    return search_quran(keyword, surah, edition)

@mcp.tool()
async def get_quran_juz(juz_number: int, edition: str = "quran-uthmani") -> dict:
    """
    Get a specific Juz (section) of the Quran.
    """
    return get_juz(juz_number, edition)

@mcp.tool()
async def get_sajda_verses(edition: str = "quran-uthmani") -> dict:
    """
    Get all Ayahs that require Sajda (prostration).
    """
    return get_sajda_ayahs(edition)

@mcp.tool()
async def get_ayah_multiple_editions(reference: str, editions: str) -> dict:
    """
    Get an Ayah in multiple editions/translations.
    """
    return get_multiple_editions(reference, editions)

if __name__ == "__main__":
    mcp.run(transport="stdio")