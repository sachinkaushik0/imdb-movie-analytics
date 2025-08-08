import pandas as pd
import json

# Paths

from config import DATA_FILE, OUTPUT_DIR

MOVIE_FILE = 'app/data/tmdb_5000_movies.csv'
CREDITS_FILE = 'app/imdb-movie-analytics/data/tmdb_5000_credits.csv'

def parse_json_column(column):
    """Safely parse a column containing stringified JSON arrays"""
    def try_parse(value):
        try:
            return [item['name'] for item in json.loads(value)]
        except Exception:
            return []
    return column.apply(try_parse)

def extract_director(crew_column):
    """Extract the director's name from the crew list"""
    def get_director(crew_json):
        try:
            crew_list = json.loads(crew_json)
            for crew in crew_list:
                if crew.get('job') == 'Director':
                    return crew.get('name')
        except:
            return None
    return crew_column.apply(get_director)

def process():
    # Load data
    movies_df = pd.read_csv(MOVIE_FILE)
    credits_df = pd.read_csv(CREDITS_FILE)

    # Quick check prints for JSON parsing (can be removed later)
    print("Sample genres:", movies_df['genres'].iloc[0])
    print("Parsed genres:", parse_json_column(movies_df['genres']).iloc[0])
    print("Sample cast:", credits_df['cast'].iloc[0])
    print("Parsed cast names:", parse_json_column(credits_df['cast']).iloc[0])
    print("Sample crew:", credits_df['crew'].iloc[0])
    print("Extracted director:", extract_director(credits_df['crew']).iloc[0])

    # Merge on movie ID
    merged_df = movies_df.merge(credits_df, left_on='id', right_on='movie_id')

    # Parse JSON columns
    merged_df['genres'] = parse_json_column(merged_df['genres'])
    merged_df['keywords'] = parse_json_column(merged_df['keywords'])
    merged_df['cast_names'] = parse_json_column(merged_df['cast'])
    merged_df['director'] = extract_director(merged_df['crew'])

    # Parse release date to datetime
    merged_df['release_date'] = pd.to_datetime(merged_df['release_date'], errors='coerce')
    merged_df['release_year'] = merged_df['release_date'].dt.year

    # Select key columns
    selected = merged_df[[
    'title_x', 'release_date', 'release_year', 'runtime', 'vote_average', 'vote_count',
    'popularity', 'revenue', 'budget', 'genres', 'keywords', 'cast_names', 'director', 'overview'
]]


    # Keep only first 500 rows
    selected = selected.head(500)

    # Save cleaned dataset
    output_path =   '/Users/sachinkaushik/PersonalProjects/imdb-movie-analytics/dataclean_movies.csv'
    selected.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    process()
