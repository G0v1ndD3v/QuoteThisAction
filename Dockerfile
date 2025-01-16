FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy repository files
COPY . /app

# Run Python script
CMD ["python", "update_readme.py"]
