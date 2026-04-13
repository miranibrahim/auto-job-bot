import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

DATA_FILE = "data/state.json"
LOG_FILE = "logs/app.log"

PRIORITY_COUNTRIES = [
    "Germany", "Bangladesh", "Japan", "Ireland",
    "Luxembourg", "UK", "USA", "Malaysia", "Singapore"
]

TELEGRAM_COUNTRIES = [
    "Germany", "Netherlands", "Bangladesh", "China", "Japan",
    "Australia", "Ireland", "Luxembourg", "UK", "Thailand",
    "Malaysia", "Singapore", "Saudi Arabia", "Taiwan",
    "Turkey", "USA"
]