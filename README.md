# git-releases-tg-notifier
# GitHub Release Notifier 🚀

GitHub Release Notifier is a simple Python script that monitors GitHub repositories for new releases and sends notifications to a Telegram chat. Perfect for staying updated on your favorite projects! 🌟

## Features
- Monitor multiple GitHub repositories for new releases.
- Sends notifications to a specified Telegram chat.
- Easy to configure via environment variables.
- Lightweight and Docker-friendly.

## Requirements
- Python 3.7 or higher
- Telegram Bot Token and Chat ID
- (Optional) GitHub Token for higher API rate limits (recommended for frequent checks)

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
GITHUB_TOKEN=your_github_token
CHECK_INTERVAL=300
REPOSITORIES=owner/repo,owner/repo2
```

### 3. Install dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Run the script
Start the script using Python:
```bash
python github_multi_repo_release_notifier.py
```

## Using Docker

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
| `GITHUB_TOKEN`        | GitHub token to increase API rate limits (optional for public repositories)| `ghp_abcdefghijklmnopqrstuvwxyz123456`  |
| `CHECK_INTERVAL`      | Interval (in seconds) for checking repositories for new releases           | `300`                                   |
| `REPOSITORIES`        | Comma-separated list of repositories in the format `owner/repo`            | `owner/repo,owner/repo2`                |

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments
- GitHub API
- Telegram Bot API

Happy monitoring! 🚀