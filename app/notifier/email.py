import smtplib
from email.mime.text import MIMEText
import time

def send_email(config, subject, html, logger):
    msg = MIMEText(html, "html")
    msg["Subject"] = subject
    msg["From"] = config.EMAIL_USER
    msg["To"] = config.EMAIL_TO

    for _ in range(3):
        try:
            with smtplib.SMTP(config.EMAIL_HOST, config.EMAIL_PORT, timeout=10) as server:
                server.starttls()
                server.login(config.EMAIL_USER, config.EMAIL_PASS)
                server.send_message(msg)

            return True

        except Exception as e:
            logger.error(f"Email error: {e}")
            time.sleep(2)

    return False