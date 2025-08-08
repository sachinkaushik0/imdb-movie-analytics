import os

if os.path.exists("/app/data/clean_movies.csv"):
    DATA_FILE = "/app/data/clean_movies.csv"
    OUTPUT_DIR = "/app/output/"
else:
    # fallback for local dev environment
    DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/clean_movies.csv"))
    OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../output"))
