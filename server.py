"""
Quran MCP Server - A Model Context Protocol server for accessing the Holy Quran
Optimized for deployment on Smithery.ai
"""

import asyncio
import json
import sys
from typing import Any, Dict

from app import (
    get_available_editions, get_surah_list, get_surah, get_ayah,
    get_random_ayah, search_quran, get_juz, get_sajda_ayahs, get_multiple_editions
)

class QuranMCPServer:
    """MCP Server for Quran API access"""

    def __init__(self):
        self.tools = {
            "get_random_quran_ayah": {
                "description": "Get a random Ayah (verse) from the Quran",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "edition": {
                            "type": "string",
                            "description": "Edition identifier (default: quran-uthmani)",
                            "default": "quran-uthmani"
                        }
                    }
                }
            },
            "get_quran_ayah": {
                "description": "Get a specific Ayah (verse) from the Quran",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reference": {
                            "type": "string",
                            "description": "Ayah reference (e.g., '2:255' for Ayat Al-Kursi)"
                        },
                        "edition": {
                            "type": "string",
                            "description": "Edition identifier (default: quran-uthmani)",
                            "default": "quran-uthmani"
                        }
                    },
                    "required": ["reference"]
                }
            },
            "get_quran_surah": {
                "description": "Get a complete Surah from the Quran",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "surah_number": {
                            "type": "integer",
                            "description": "Surah number (1-114)"
                        },
                        "edition": {
                            "type": "string",
                            "description": "Edition identifier (default: quran-uthmani)",
                            "default": "quran-uthmani"
                        }
                    },
                    "required": ["surah_number"]
                }
            },
            "list_quran_editions": {
                "description": "Get list of all available Quran editions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "format_type": {
                            "type": "string",
                            "description": "Format filter: 'text' or 'audio'"
                        },
                        "language": {
                            "type": "string",
                            "description": "2-digit language code (e.g., 'en', 'ar')"
                        },
                        "edition_type": {
                            "type": "string",
                            "description": "Type filter: 'translation', 'tafsir', etc."
                        }
                    }
                }
            },
            "list_quran_surahs": {
                "description": "Get list of all Surahs in the Quran",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            },
            "search_quran_text": {
                "description": "Search for a keyword in the Quran text",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "Search term"
                        },
                        "surah": {
                            "type": "string",
                            "description": "Surah number (1-114) or 'all' (default: all)",
                            "default": "all"
                        },
                        "edition": {
                            "type": "string",
                            "description": "Edition identifier or language code (default: en)",
                            "default": "en"
                        }
                    },
                    "required": ["keyword"]
                }
            },
            "get_quran_juz": {
                "description": "Get a specific Juz (section) of the Quran",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "juz_number": {
                            "type": "integer",
                            "description": "Juz number (1-30)"
                        },
                        "edition": {
                            "type": "string",
                            "description": "Edition identifier (default: quran-uthmani)",
                            "default": "quran-uthmani"
                        }
                    },
                    "required": ["juz_number"]
                }
            },
            "get_sajda_verses": {
                "description": "Get all Ayahs that require Sajda (prostration)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "edition": {
                            "type": "string",
                            "description": "Edition identifier (default: quran-uthmani)",
                            "default": "quran-uthmani"
                        }
                    }
                }
            },
            "get_ayah_multiple_editions": {
                "description": "Get an Ayah in multiple editions/translations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reference": {
                            "type": "string",
                            "description": "Ayah reference (e.g., '2:255')"
                        },
                        "editions": {
                            "type": "string",
                            "description": "Comma-separated edition identifiers"
                        }
                    },
                    "required": ["reference", "editions"]
                }
            }
        }

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP requests"""
        method = request.get("method")
        params = request.get("params", {})

        if method == "tools/list":
            return {
                "tools": [
                    {"name": name, **tool_def}
                    for name, tool_def in self.tools.items()
                ]
            }

        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})

            if tool_name == "get_random_quran_ayah":
                result = get_random_ayah(arguments.get("edition", "quran-uthmani"))
            elif tool_name == "get_quran_ayah":
                result = get_ayah(arguments["reference"], arguments.get("edition", "quran-uthmani"))
            elif tool_name == "get_quran_surah":
                result = get_surah(arguments["surah_number"], arguments.get("edition", "quran-uthmani"))
            elif tool_name == "list_quran_editions":
                result = get_available_editions(
                    arguments.get("format_type"),
                    arguments.get("language"),
                    arguments.get("edition_type")
                )
            elif tool_name == "list_quran_surahs":
                result = get_surah_list()
            elif tool_name == "search_quran_text":
                result = search_quran(
                    arguments["keyword"],
                    arguments.get("surah", "all"),
                    arguments.get("edition", "en")
                )
            elif tool_name == "get_quran_juz":
                result = get_juz(arguments["juz_number"], arguments.get("edition", "quran-uthmani"))
            elif tool_name == "get_sajda_verses":
                result = get_sajda_ayahs(arguments.get("edition", "quran-uthmani"))
            elif tool_name == "get_ayah_multiple_editions":
                result = get_multiple_editions(arguments["reference"], arguments["editions"])
            else:
                return {"error": f"Unknown tool: {tool_name}"}

            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(result, indent=2, ensure_ascii=False)
                    }
                ]
            }

        return {"error": f"Unknown method: {method}"}

    async def run_stdio(self):
        """Run the server using stdio transport"""
        while True:
            try:
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break

                request = json.loads(line.strip())
                response = await self.handle_request(request)

                print(json.dumps(response, ensure_ascii=False))
                sys.stdout.flush()

            except json.JSONDecodeError:
                print(json.dumps({"error": "Invalid JSON"}))
                sys.stdout.flush()
            except Exception as e:
                print(json.dumps({"error": str(e)}))
                sys.stdout.flush()

async def main():
    """Main entry point"""
    server = QuranMCPServer()
    await server.run_stdio()

if __name__ == "__main__":
    asyncio.run(main())