import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import DATA_FILE, OUTPUT_DIR
DATA_FILE = "/app/data/clean_movies.csv"
OUTPUT_DIR = "/app/output/"



print(f"Using DATA_FILE: {DATA_FILE}")
print(f"Using OUTPUT_DIR: {OUTPUT_DIR}")

def run_eda():
    df = pd.read_csv(DATA_FILE)

    # Ensure genres are lists
    df['genres'] = df['genres'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    # 1️⃣ Overview stats
    print("Dataset shape:", df.shape)
    print("\nNumeric summary:\n", df.describe())

    # 2️⃣ Top 10 genres by movie count
    all_genres = pd.Series([g for sublist in df['genres'] for g in sublist])
    top_genres = all_genres.value_counts().head(10)
    plt.figure(figsize=(8,5))
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
    plt.title("Top 10 Genres by Movie Count")
    plt.xlabel("Number of Movies")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "top_genres.png")
    plt.close()

    # 3️⃣ Revenue vs Budget
    plt.figure(figsize=(6,6))
    sns.scatterplot(data=df, x='budget', y='revenue', alpha=0.5)
    plt.title("Budget vs Revenue")
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "budget_vs_revenue.png")
    plt.close()

    # 4️⃣ Ratings distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df['vote_average'], bins=20, kde=True, color='skyblue')
    plt.title("Distribution of Vote Averages")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "ratings_distribution.png")
    plt.close()

    # 5️⃣ Popularity over time
    yearly_popularity = df.groupby('release_year')['popularity'].mean().dropna()
    plt.figure(figsize=(10,5))
    sns.lineplot(x=yearly_popularity.index, y=yearly_popularity.values)
    plt.title("Average Popularity by Year")
    plt.xlabel("Year")
    plt.ylabel("Popularity")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "popularity_over_time.png")
    plt.close()

    # 6️⃣ Save quick summary
    summary_text = f"""
    TMDB Dataset EDA Summary
    -------------------------
    Total movies: {df.shape[0]}

    Top Genres:
    {top_genres.to_string()}

    Average rating: {df['vote_average'].mean():.2f}
    Average budget: {df['budget'].mean():.2f}
    Average revenue: {df['revenue'].mean():.2f}
    """
    with open(OUTPUT_DIR + "eda_summary.txt", 'w') as f:
        f.write(summary_text)

    print("✅ EDA complete. Plots and summary saved in output folder.")

if __name__ == "__main__":
    run_eda()
