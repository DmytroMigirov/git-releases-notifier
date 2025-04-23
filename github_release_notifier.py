import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
# Read repositories from .env and split them into a list
REPOSITORIES = os.getenv("REPOSITORIES", "").split(",")  # Default to an empty list if not provided
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))  # Default interval is 300 seconds

# Telegram API endpoint for sending messages
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# GitHub API headers
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else None,
    "Accept": "application/vnd.github.v3+json"
}

def get_latest_release(repo):
    """
    Fetch the latest release from GitHub for a given repository.
    :param repo: Repository in the format "owner/repo"
    :return: JSON response with release details or None in case of an error
    """
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"⚠️ Error fetching data from GitHub API for {repo}: {response.status_code}")
        return None

def send_telegram_message(message):
    """
    Send a message to a Telegram chat using the bot.
    :param message: The message text to send
    """
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # Enables Markdown formatting in messages
    }
    response = requests.post(TELEGRAM_API_URL, json=payload)
    if response.status_code == 200:
        print("✅ Message successfully sent to Telegram.")
    else:
        print(f"⚠️ Error sending message to Telegram: {response.status_code}")

def main():
    """
    Main function to monitor repositories for new releases and send notifications.
    """
    # Store the last release ID for each repository
    last_release_ids = {repo: None for repo in REPOSITORIES}

    while True:
        for repo in REPOSITORIES:
            # Fetch the latest release for the repository
            release = get_latest_release(repo)
            if release:
                release_id = release.get("id")
                # Check if the release is new
                if release_id != last_release_ids[repo]:
                    last_release_ids[repo] = release_id
                    release_name = release.get("name", "No name")
                    release_tag = release.get("tag_name", "No tag")
                    release_url = release.get("html_url", "No URL")
                    # Prepare the notification message
                    message = (
                        f"🚀 *New Release Alert!* 🛠️\n\n"
                        f"📦 Repository: `{repo}`\n"
                        f"🏷️ Name: *{release_name}*\n"
                        f"🔖 Tag: `{release_tag}`\n"
                        f"🔗 [View Release]({release_url})\n\n"
                        f"Stay tuned for updates! 🌟"
                    )
                    # Send the message to Telegram
                    send_telegram_message(message)
        # Wait for the specified interval before checking again
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()