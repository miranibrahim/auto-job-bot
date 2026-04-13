import requests
import time

def send_telegram(token, chat_id, message, logger):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    for attempt in range(3):
        try:
            r = requests.post(url, json={
                "chat_id": chat_id,
                "text": message
            }, timeout=10)

            logger.info(f"Telegram response: {r.text}")

            if r.status_code == 200:
                return True

        except Exception as e:
            logger.error(f"Telegram error: {e}")

        time.sleep(2)

    return False