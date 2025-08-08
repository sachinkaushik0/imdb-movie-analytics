# TMDB Movie Analytics

Analyze and visualize movie metadata from the TMDB Kaggle dataset. This project includes data cleaning, exploratory data analysis (EDA), and an interactive Streamlit dashboard to explore movie trends by decade, rating, and popularity.
<img width="1304" height="836" alt="image" src="https://github.com/user-attachments/assets/4ff205a8-deb8-4178-9498-f01eaad55971" />

---

## 📊 Project Overview

This repository hosts a comprehensive analysis pipeline for the TMDB movie dataset, covering:

- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA) with visualizations  
- Interactive Streamlit dashboard for filtering and exploring movies  
- Docker support for reproducible environments  

---

## 📂 Data

The dataset is sourced from [TMDB Movie Metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).  
It contains detailed metadata for 5000+ movies, including:

- Title, release date/year  
- Runtime, genres, keywords  
- Ratings, popularity, revenue, budget  
- Cast and director information  

---

## ⚙️ Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tmdb-movie-analytics.git
   cd tmdb-movie-analytics
(Optional) Create and activate a Python virtual environment:


python3 -m venv myenv
source myenv/bin/activate   # macOS/Linux
myenv\Scripts\activate      # Windows
Install required Python packages:

pip install -r requirements.txt
Download the dataset files from Kaggle and place them inside the data/ folder.

🚀 Running the Project
Run Exploratory Data Analysis (EDA)

python src/eda-tmdb.py
This script loads cleaned movie data and generates summary statistics and visualizations saved in the output/ directory.

Launch the Streamlit Dashboard

streamlit run src/app.py
Interactive dashboard to filter movies by decade, rating, and popularity with dynamic plots and tables.

🐳 Using Docker (Recommended for Reproducibility)
Build the Docker image:
docker build -t tmdb-analytics .
Run the container with mounted data and output folders:

docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/output:/app/output -p 8501:8501 tmdb-analytics streamlit run src/app.py
Open your browser at http://localhost:8501 to access the dashboard.

🗂️ Project Structure

tmdb-movie-analytics/
│
├── data/                  # Raw and cleaned datasets (not tracked in Git)
├── output/                # EDA outputs and dashboard saved files
├── src/
│   ├── eda-tmdb.py        # Exploratory Data Analysis script
│   ├── app.py             # Streamlit dashboard app
│   └── ...                # Additional scripts or modules
├── Dockerfile             # Docker setup
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files/folders to ignore in Git

📈 Key Features
Clean and enrich TMDB movie dataset

Visual EDA with distribution plots, correlation analysis

Interactive dashboard with filtering options

Dockerized environment for consistent runs across machines

📋 Future Improvements
Add user authentication and save personalized views

Enhance dashboard with additional charts (e.g., revenue trends)

Integrate with other movie datasets for richer insights

Deploy the dashboard on cloud platforms (Streamlit Cloud, Heroku, etc.)

📞 Contact
Created by Sachin Kaushik
LinkedIn | sachinkaushikca@gmail.com

Enjoy exploring the movie data! 🍿🎬
