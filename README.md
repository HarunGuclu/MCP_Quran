# Quran MCP Server

A Model Context Protocol (MCP) server that provides access to the Holy Quran through the AlQuran.cloud API. This server allows AI assistants to retrieve Quranic verses, search the text, and access various translations and recitations.

## Features

- **Random Ayah**: Get random verses from the Quran
- **Specific Ayah**: Retrieve specific verses by reference (e.g., "2:255" for Ayat Al-Kursi)
- **Complete Surahs**: Get entire chapters with all verses
- **Multiple Editions**: Access Arabic text, translations, and audio recitations
- **Search Functionality**: Search for keywords across the Quran
- **Juz Access**: Retrieve specific sections (Juz) of the Quran
- **Sajda Verses**: Get all verses requiring prostration
- **Multi-language Support**: Available in multiple languages and translations

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Test the API functions (optional):
```bash
python test_api.py
```

3. Run the server:
```bash
python -m server
```

Or use the provided batch file on Windows:
```bash
run.bat
```

The batch file provides a menu with options to:
- Install dependencies
- Test API functions
- Start the MCP server
- Exit

## Available Tools

### 1. get_random_quran_ayah
Get a random Ayah from the Quran.
- **Parameters**: `edition` (optional, default: "quran-uthmani")
- **Example**: Get random verse in English translation

### 2. get_quran_ayah
Get a specific Ayah by reference.
- **Parameters**: `reference` (required), `edition` (optional)
- **Example**: `reference="2:255"` for Ayat Al-Kursi

### 3. get_quran_surah
Get a complete Surah.
- **Parameters**: `surah_number` (1-114), `edition` (optional)
- **Example**: `surah_number=1` for Al-Fatiha

### 4. list_quran_editions
List available translations and recitations.
- **Parameters**: `format_type`, `language`, `edition_type` (all optional)
- **Example**: Filter by language="en" for English editions

### 5. list_quran_surahs
Get list of all 114 Surahs.
- **Parameters**: None
- **Returns**: Complete list with names and metadata

### 6. search_quran_text
Search for keywords in the Quran.
- **Parameters**: `keyword` (required), `surah` (optional), `edition` (optional)
- **Example**: Search for "mercy" across all Surahs

### 7. get_quran_juz
Get a specific Juz (section).
- **Parameters**: `juz_number` (1-30), `edition` (optional)
- **Example**: Get the 30th Juz

### 8. get_sajda_verses
Get all verses requiring prostration.
- **Parameters**: `edition` (optional)
- **Returns**: All 15 Sajda verses

### 9. get_ayah_multiple_editions
Get an Ayah in multiple translations.
- **Parameters**: `reference`, `editions` (comma-separated)
- **Example**: Compare translations side by side

## Popular Editions

### Arabic Text
- `quran-uthmani`: Standard Arabic text
- `quran-simple`: Simplified Arabic text

### English Translations
- `en.asad`: Muhammad Asad translation
- `en.pickthall`: Marmaduke Pickthall translation
- `en.sahih`: Sahih International translation
- `en.yusufali`: Abdullah Yusuf Ali translation

### Audio Recitations
- `ar.alafasy`: Mishary Alafasy recitation
- `ar.husary`: Mahmoud Khalil Al-Husary recitation

## API Reference

This server uses the AlQuran.cloud API (https://alquran.cloud/api) which provides:
- 114 Surahs (chapters)
- 6,236 Ayahs (verses)
- 30 Juz (sections)
- Multiple languages and translations
- Audio recitations

## Usage Examples

1. **Get Ayat Al-Kursi in multiple translations**:
   ```
   get_ayah_multiple_editions(reference="2:255", editions="quran-uthmani,en.asad,en.pickthall")
   ```

2. **Search for "Abraham" in English**:
   ```
   search_quran_text(keyword="Abraham", edition="en")
   ```

3. **Get the opening chapter (Al-Fatiha)**:
   ```
   get_quran_surah(surah_number=1, edition="en.asad")
   ```

## License

This project uses the AlQuran.cloud API which is provided by Islamic Network.

## Project Structure

- **app.py**: Core API functions for interacting with AlQuran.cloud API
- **server.py**: MCP server implementation with tool definitions
- **smithery.yaml**: MCP configuration file
- **requirements.txt**: Python dependencies
- **run.bat**: Windows batch file for easy server management
- **test_api.py**: Test script for API functions
- **test_mcp_server.py**: Test script for MCP server functionality
- **simple_test.py**: Simple test for server components
- **README.md**: This documentation file

## Contributing

Feel free to submit issues and enhancement requests!
