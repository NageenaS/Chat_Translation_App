# Use the official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Upgrade pip first
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
