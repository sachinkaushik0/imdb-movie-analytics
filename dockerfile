# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code and requirements
COPY requirements.txt requirements.txt
COPY src/ src/
COPY data/ data/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the scraping script
CMD ["python", "src/scrape_imdb.py"]
