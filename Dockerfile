# Use a minimal base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY github_release_notifier.py .

# Default command to run the script
CMD ["python", "github_release_notifier.py"]