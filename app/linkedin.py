import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

BASE_URL = "https://www.linkedin.com/jobs/search/"

KEYWORDS = (
    '"backend developer" AND (junior OR mid) AND '
    '(PHP OR Laravel OR Python) AND '
    '(Java OR "Spring Boot") AND '
    '(Node.js OR JavaScript OR Typescript) AND OOP'
)

def build_url(country, remote_only=False):
    query = KEYWORDS

    if not remote_only:
        query += ' AND ("visa sponsorship" OR relocation)'

    params = {
        "keywords": query,
        "location": country,
        "f_TPR": "r86400",
        "sortBy": "DD",
        "f_WT": "2" if remote_only else "1,2"
    }

    query_string = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"{BASE_URL}?{query_string}"

def fetch_jobs(url, logger):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return []

        soup = BeautifulSoup(r.text, "html.parser")

        jobs = []
        cards = soup.select(".base-card")

        for c in cards[:5]:  # lightweight only
            try:
                title = c.select_one(".base-search-card__title").text.strip()
                company = c.select_one(".base-search-card__subtitle").text.strip()
                link = c.select_one("a")["href"]

                jobs.append({
                    "title": title,
                    "company": company,
                    "link": link
                })
            except:
                continue

        return jobs

    except Exception as e:
        logger.warning(f"Scraping failed: {e}")
        return []