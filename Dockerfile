FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and .env file
COPY github_release_notifier.py github_release_notifier.py
COPY .env .env

# Default command to run the script
CMD ["python", "github_release_notifier.py"]