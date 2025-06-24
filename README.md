# GitHub Release Notifier 🚀

GitHub Release Notifier is a simple Python script that monitors GitHub repositories for new releases and sends notifications to Telegram, Slack, or both. Perfect for staying updated on your favorite projects! 🌟

## Features
- Monitor multiple GitHub repositories for new releases.
- Sends notifications to Telegram, Slack, or both (configurable).
- Easy to configure via environment variables.
- Lightweight and Docker-friendly.

## Requirements
- Python 3.7 or higher
- Telegram Bot Token and Chat ID
- (Optional) Slack Webhook URL for Slack notifications
- (Optional) GitHub Token for higher API rate limits (recommended for frequent checks)

<hr></hr>

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/github-release-notifier.git
cd github-release-notifier
```

### 2. Create the `.env` file
Copy the `.env.example` file to `.env` and fill in the required values:
```bash
cp .env.example .env
```

Edit the `.env` file and replace placeholders with your actual values:
```plaintext
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/webhook/url
NOTIFICATION_CHANNELS=telegram,slack
GITHUB_TOKEN=your_github_token
CHECK_INTERVAL=300
REPOSITORIES=owner/repo,owner/repo2
```
<hr></hr>

## Running Locally

### 3. Install dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Run the script
Start the script using Python:
```bash
python github_release_notifier.py
```
<hr></hr>

## Running using Docker

### Build the Docker image
```bash
docker build -t github-release-notifier .
```

### Run the container
```bash
docker run -d --name release-notifier --env-file .env github-release-notifier
```

### Restart policy (optional)
To ensure the container restarts automatically after a failure or server reboot:
```bash
docker run -d --restart always --name release-notifier --env-file .env github-release-notifier
```

## Environment Variables
| Variable              | Description                                                                 | Example                                 |
|-----------------------|-----------------------------------------------------------------------------|-----------------------------------------|
| `TELEGRAM_BOT_TOKEN`  | Telegram bot token for sending notifications                               | `123456789:ABC-defGHIjklMNOpqRSTuvWXyz` |
| `TELEGRAM_CHAT_ID`    | Chat ID where notifications will be sent                                   | `123456789`                             |
| `SLACK_WEBHOOK_URL`   | Slack Webhook URL for sending notifications                                | `https://hooks.slack.com/services/...`  |
| `NOTIFICATION_CHANNELS` | Comma-separated list of notification channels (`telegram`, `slack`, or both) | `telegram,slack`                        |
| `GITHUB_TOKEN`        | GitHub token to increase API rate limits (optional for public repositories)| `ghp_abcdefghijklmnopqrstuvwxyz123456`  |
| `CHECK_INTERVAL`      | Interval (in seconds) for checking repositories for new releases           | `300`                                   |
| `REPOSITORIES`        | Comma-separated list of repositories in the format `owner/repo`            | `owner/repo,owner/repo2`                |

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- GitHub API
- Telegram Bot API
- Slack Incoming Webhooks

Happy monitoring! 🚀