import requests
import random

def get_available_editions(format_type=None, language=None, edition_type=None):
    """
    Get list of available Quran editions (translations/recitations).

    Args:
        format_type (str, optional): 'text' or 'audio'
        language (str, optional): 2-digit language code (e.g., 'en', 'ar')
        edition_type (str, optional): 'translation', 'tafsir', etc.

    Returns:
        dict: Available editions data or error message
    """
    url = "http://api.alquran.cloud/v1/edition"

    params = {}
    if format_type:
        params['format'] = format_type
    if language:
        params['language'] = language
    if edition_type:
        params['type'] = edition_type

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve editions. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_surah_list():
    """
    Get list of all Surahs in the Quran.

    Returns:
        dict: List of Surahs or error message
    """
    url = "http://api.alquran.cloud/v1/surah"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve surah list. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_surah(surah_number, edition="quran-uthmani"):
    """
    Get a specific Surah with translation/edition.

    Args:
        surah_number (int): Surah number (1-114)
        edition (str): Edition identifier (default: "quran-uthmani" for Arabic text)

    Returns:
        dict: Surah data or error message
    """
    url = f"http://api.alquran.cloud/v1/surah/{surah_number}/{edition}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve surah. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_ayah(reference, edition="quran-uthmani"):
    """
    Get a specific Ayah (verse) with translation/edition.

    Args:
        reference (str): Ayah reference (e.g., "2:255" or "262")
        edition (str): Edition identifier (default: "quran-uthmani")

    Returns:
        dict: Ayah data or error message
    """
    url = f"http://api.alquran.cloud/v1/ayah/{reference}/{edition}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve ayah. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_random_ayah(edition="quran-uthmani"):
    """
    Get a random Ayah from the Quran.

    Args:
        edition (str): Edition identifier (default: "quran-uthmani")

    Returns:
        dict: Random Ayah data or error message
    """
    # Generate random ayah number (1-6236)
    random_ayah = random.randint(1, 6236)
    return get_ayah(str(random_ayah), edition)

def search_quran(keyword, surah="all", edition="en"):
    """
    Search for a keyword in the Quran text.

    Args:
        keyword (str): Search keyword
        surah (str): Surah number (1-114) or "all" to search all
        edition (str): Edition identifier or language code (default: "en")

    Returns:
        dict: Search results or error message
    """
    url = f"http://api.alquran.cloud/v1/search/{keyword}/{surah}/{edition}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to search. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_juz(juz_number, edition="quran-uthmani"):
    """
    Get a specific Juz (section) of the Quran.

    Args:
        juz_number (int): Juz number (1-30)
        edition (str): Edition identifier (default: "quran-uthmani")

    Returns:
        dict: Juz data or error message
    """
    url = f"http://api.alquran.cloud/v1/juz/{juz_number}/{edition}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve juz. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_sajda_ayahs(edition="quran-uthmani"):
    """
    Get all Ayahs that require Sajda (prostration).

    Args:
        edition (str): Edition identifier (default: "quran-uthmani")

    Returns:
        dict: Sajda Ayahs data or error message
    """
    url = f"http://api.alquran.cloud/v1/sajda/{edition}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve sajda ayahs. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_multiple_editions(reference, editions):
    """
    Get an Ayah or Surah in multiple editions.

    Args:
        reference (str): Ayah or Surah reference
        editions (str): Comma-separated edition identifiers

    Returns:
        dict: Multi-edition data or error message
    """
    url = f"http://api.alquran.cloud/v1/ayah/{reference}/editions/{editions}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve multi-edition data. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}
