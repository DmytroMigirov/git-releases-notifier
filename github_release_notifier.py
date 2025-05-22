import os
import requests
import time
import logging
from dotenv import load_dotenv

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Log to file
        logging.StreamHandler()         # Log to console
    ]
)

# Load environment variables from .env file
load_dotenv()

# Application configuration
REPOSITORIES = os.getenv("REPOSITORIES", "").split(",")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))

# Telegram API URL for sending messages
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# GitHub API headers
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else None,
    "Accept": "application/vnd.github.v3+json"
}

def get_latest_release(repo):
    """
    Fetch the latest release information for a given repository.
    """
    logging.info(f"Fetching latest release for repository: {repo}")
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        logging.info(f"Successfully fetched release data for {repo}")
        return response.json()
    else:
        logging.error(f"Error fetching data from GitHub API for {repo}: {response.status_code}")
        return None

def send_telegram_message(message):
    """
    Send a message to the configured Telegram chat.
    """
    logging.info("Sending message to Telegram...")
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(TELEGRAM_API_URL, json=payload)
    if response.status_code == 200:
        logging.info("Message successfully sent to Telegram.")
    else:
        logging.error(f"Error sending message to Telegram: {response.status_code}")

def main():
    """
    Main function to monitor GitHub repositories for new releases
    and notify via Telegram.
    """
    logging.info("Starting GitHub release notifier...")
    last_release_ids = {repo: None for repo in REPOSITORIES}

    while True:
        for repo in REPOSITORIES:
            release = get_latest_release(repo)
            if release:
                release_id = release.get("id")
                if release_id != last_release_ids[repo]:
                    last_release_ids[repo] = release_id
                    release_name = release.get("name", "No name")
                    release_tag = release.get("tag_name", "No tag")
                    release_url = release.get("html_url", "No URL")
                    message = (
                        f"🚀 *New Release Alert!* 🛠️\n\n"
                        f"📦 Repository: `{repo}`\n"
                        f"🏷️ Name: *{release_name}*\n"
                        f"🔖 Tag: `{release_tag}`\n"
                        f"🔗 [View Release]({release_url})\n\n"
                        f"Stay tuned for updates! 🌟"
                    )
                    send_telegram_message(message)
        logging.info(f"Sleeping for {CHECK_INTERVAL} seconds...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()