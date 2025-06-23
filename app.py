import requests
import random

# Kuran API Base URL
QURAN_API_BASE = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1"

def get_editions():
    """
    Mevcut tüm Kuran sürümlerini güzelleştirilmiş JSON biçiminde listeler.
    Lists all available Quran editions in pretty JSON format.

    Returns / Dönüş:
        dict: Sürümler listesi veya hata mesajı / List of editions or error message

    Örnek / Example:
        >>> get_editions()
        {'en-sahih': {...}, 'tr-ates': {...}, ...}
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/editions.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve editions. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_editions_min():
    """
    Mevcut tüm Kuran sürümlerinin küçültülmüş (minified) versiyonunu getirir.
    Lists all available Quran editions in minified JSON format.

    Returns / Dönüş:
        dict: Küçültülmüş sürümler listesi veya hata mesajı / Minified list of editions or error message

    Örnek / Example:
        >>> get_editions_min()
        {'en-sahih': {...}, 'tr-ates': {...}, ...}
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/editions.min.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve editions (min). Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_full_quran(edition_name: str, script_type: str = ""):
    """
    Tüm Kuran'ı veya Kuran tercümesini getirir.
    Gets the full Quran or translation.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates", "en-sahih") / Edition name (e.g. "tr-ates", "en-sahih")
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Kuran verisi veya hata mesajı / Quran data or error message

    Örnek / Example:
        >>> get_full_quran("tr-ates")
        {'chapter': {...}, ...}
        >>> get_full_quran("ar-mujawwad", "la")
        {'chapter': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve full Quran. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_chapter(edition_name: str, chapter_no: int, script_type: str = "", minified: bool = False):
    """
    Belirtilen bölümün (sure) tamamını getirir.
    Gets the full chapter (surah).

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        chapter_no (int): Bölüm numarası (1-114) / Chapter number (1-114)
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)
        minified (bool, optional): Küçültülmüş format isteniyor mu / Whether minified format is requested

    Returns / Dönüş:
        dict: Sure verisi veya hata mesajı / Chapter data or error message

    Örnek / Example:
        >>> get_chapter("tr-ates", 1)
        {'chapter': {...}, ...}
        >>> get_chapter("ar-mujawwad", 2, "la", True)
        {'chapter': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        min_suffix = ".min" if minified else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/{chapter_no}{min_suffix}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve chapter. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_verse(edition_name: str, chapter_no: int, verse_no: int, script_type: str = ""):
    """
    Belirtilen ayeti getirir.
    Gets the specified verse.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        chapter_no (int): Bölüm numarası (1-114) / Chapter number (1-114)
        verse_no (int): Ayet numarası / Verse number
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Ayet verisi veya hata mesajı / Verse data or error message

    Örnek / Example:
        >>> get_verse("tr-ates", 1, 1)
        {'verse': {...}, ...}
        >>> get_verse("ar-mujawwad", 2, 255, "la")
        {'verse': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/{chapter_no}/{verse_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve verse. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_juz(edition_name: str, juz_no: int, script_type: str = ""):
    """
    Belirtilen cüzü getirir.
    Gets the specified juz.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        juz_no (int): Cüz numarası (1-30) / Juz number (1-30)
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Cüz verisi veya hata mesajı / Juz data or error message

    Örnek / Example:
        >>> get_juz("tr-ates", 1)
        {'juz': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/juzs/{juz_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve juz. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_ruku(edition_name: str, ruku_no: int, script_type: str = ""):
    """
    Belirtilen rükuyu getirir.
    Gets the specified ruku.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        ruku_no (int): Rüku numarası / Ruku number
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Rüku verisi veya hata mesajı / Ruku data or error message

    Örnek / Example:
        >>> get_ruku("tr-ates", 5)
        {'ruku': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/rukus/{ruku_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve ruku. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_page(edition_name: str, page_no: int, script_type: str = ""):
    """
    Belirtilen sayfayı getirir.
    Gets the specified page.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        page_no (int): Sayfa numarası / Page number
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Sayfa verisi veya hata mesajı / Page data or error message

    Örnek / Example:
        >>> get_page("tr-ates", 10)
        {'page': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/pages/{page_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve page. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_manzil(edition_name: str, manzil_no: int, script_type: str = ""):
    """
    Belirtilen menzili getirir.
    Gets the specified manzil.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        manzil_no (int): Menzil numarası (1-7) / Manzil number (1-7)
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Menzil verisi veya hata mesajı / Manzil data or error message

    Örnek / Example:
        >>> get_manzil("tr-ates", 2)
        {'manzil': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/manzils/{manzil_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve manzil. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_maqra(edition_name: str, maqra_no: int, script_type: str = ""):
    """
    Belirtilen makrayı getirir.
    Gets the specified maqra.

    Args / Parametreler:
        edition_name (str): Sürüm adı (örn: "tr-ates") / Edition name (e.g. "tr-ates")
        maqra_no (int): Makra numarası / Maqra number
        script_type (str, optional): Yazı tipi ("" = normal, "la" = latin, "lad" = latin diakritikli) / Script type ("" = normal, "la" = latin, "lad" = latin with diacritics)

    Returns / Dönüş:
        dict: Makra verisi veya hata mesajı / Maqra data or error message

    Örnek / Example:
        >>> get_maqra("tr-ates", 3)
        {'maqra': {...}, ...}
    """
    try:
        suffix = f"-{script_type}" if script_type else ""
        url = f"{QURAN_API_BASE}/editions/{edition_name}{suffix}/maqras/{maqra_no}.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve maqra. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_quran_info():
    """
    Kuran'daki cüz sayısı, secdeler, rükular vb. gibi Kuran hakkında tüm ayrıntıları getirir.
    Gets all details about the Quran such as number of juz, sajdas, rukus, etc.

    Returns / Dönüş:
        dict: Kuran hakkında bilgi veya hata mesajı / Quran info or error message

    Örnek / Example:
        >>> get_quran_info()
        {'juzs': 30, 'rukus': 558, ...}
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/info.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve Quran info. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

def get_fonts():
    """
    Mevcut Arapça yazı tiplerini listeler.
    Lists available Arabic fonts.

    Returns / Dönüş:
        dict: Yazı tipleri veya hata mesajı / Fonts or error message

    Örnek / Example:
        >>> get_fonts()
        {'fonts': ['me_quran', 'uthmani', ...]}
    """
    try:
        response = requests.get(f"{QURAN_API_BASE}/fonts.json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve fonts. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Exception occurred: {str(e)}"}

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
