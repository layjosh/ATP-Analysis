import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_match_links(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    matches = []

    for suburl in soup.find_all("a", href=True):
        match_text = suburl.get_text(strip=True)
        href = suburl["href"]

        if "(ATP)" in match_text or "(WTA)" in match_text:
            full_link = urljoin(url, href)

            matches.append({
                "match_name": match_text,
                "link": full_link
            })

    return matches
