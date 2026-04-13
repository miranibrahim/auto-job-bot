from config import *
from linkedin import build_url, fetch_jobs
from storage import Storage
from utils import setup_logger
from notifier.telegram import send_telegram
from notifier.email import send_email

logger = setup_logger(LOG_FILE)
storage = Storage(DATA_FILE)

REMOTE_ONLY = [
    "Yemen", "Oman", "Egypt", "Kuwait", "Qatar",
    "Albania", "Belgium", "Latvia", "Portugal", "Romania"
]

ALL_COUNTRIES = REMOTE_ONLY + [
    "Bangladesh", "China", "Japan", "Australia", "New Zealand",
    "Denmark", "Finland", "France", "Germany", "Greece",
    "Hungary", "Ireland", "Italy", "Luxembourg", "Netherlands",
    "Norway", "Spain", "UK", "Sweden", "USA", "Thailand",
    "Malaysia", "Singapore", "Saudi Arabia", "Taiwan", "Turkey"
]

def run():
    email_html = "<h2>Job Report</h2>"

    for country in ALL_COUNTRIES:
        remote_only = country in REMOTE_ONLY
        url = build_url(country, remote_only)

        jobs = fetch_jobs(url, logger)
        job_count = len(jobs)

        prev = storage.get_previous_count(country)

        logger.info(f"{country}: {job_count} jobs")

        # Telegram alert
        if country in TELEGRAM_COUNTRIES and job_count > prev:
            message = f"🚀 {country} Jobs\n{job_count} jobs found\n🔗 {url}"
            send_telegram(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message, logger)

        # Email content
        email_html += f"<h3>{country}</h3>"

        if jobs:
            for j in jobs:
                email_html += f"<p>{j['title']} - {j['company']}<br><a href='{j['link']}'>Apply</a></p>"
        else:
            email_html += f"<p>No jobs parsed. <a href='{url}'>Search here</a></p>"

        storage.update_country(country, job_count)

    send_email(__import__("config"), "Daily Job Report", email_html, logger)

if __name__ == "__main__":
    run()