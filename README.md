# LinkedIn Job Bot 🚀

## Overview
Automated job search system that:
- Generates LinkedIn job links
- Attempts lightweight scraping
- Falls back safely if blocked
- Sends Telegram + Email alerts

## Features
- Anti-block safe
- Dockerized
- CI/CD ready
- Zero paid services

## Setup

### Local
cp .env.example .env
pip install -r requirements.txt
python app/main.py

### Docker
docker compose up --build

## Cron
0 */12 * * * docker compose run --rm app

## GitHub Actions
1. Go to Settings → Secrets
2. Add:
   - TELEGRAM_BOT_TOKEN
   - EMAIL credentials
3. Enable Actions tab

## Logs
Check:
logs/app.log

## Example Output
🚀 Germany Jobs
12 jobs found
🔗 https://linkedin.com/jobs/...