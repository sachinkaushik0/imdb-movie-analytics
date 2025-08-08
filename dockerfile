FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code into container
COPY src /app/src

# Create output and data directories inside container
RUN mkdir -p /app/output /app/data

# Default command (optional, override in docker run)
CMD ["python", "src/eda-tmdb.py"]
