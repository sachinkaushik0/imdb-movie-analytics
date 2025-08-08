import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "/Users/sachinkaushik/PersonalProjects/imdb-movie-analytics/data/clean_movies.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    # Convert genres from string representation of list to actual list
    df['genres'] = df['genres'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    # Add decade column based on release_year
    df['decade'] = (df['release_year'] // 10) * 10
    return df

def main():
    st.title("TMDB Movie Analytics Dashboard")

    df = load_data()

    # Sidebar filters
    decades = sorted(df['decade'].dropna().unique())
    selected_decade = st.sidebar.selectbox("Select Decade", options=decades, index=decades.index(2000) if 2000 in decades else 0)

    rating_min, rating_max = st.sidebar.slider(
        "Rating range",
        float(df['vote_average'].min()), float(df['vote_average'].max()),
        (5.0, 8.0)
    )

    top_n = st.sidebar.number_input("Top N movies to display", min_value=5, max_value=50, value=10)

    # Filter data based on user selections
    filtered_df = df[
        (df['decade'] == selected_decade) &
        (df['vote_average'] >= rating_min) &
        (df['vote_average'] <= rating_max)
    ].sort_values('vote_average', ascending=False).head(top_n)

    st.subheader(f"Top {top_n} Movies from {selected_decade}s")

    # Bar plot of vote_average vs movie title_x
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='vote_average', y='title_x', data=filtered_df, palette='viridis', ax=ax)
    ax.set_xlabel("Average Vote")
    ax.set_ylabel("Movie Title")
    st.pyplot(fig)

    # Show filtered data table with relevant columns
    st.dataframe(filtered_df[['title_x', 'release_year', 'vote_average', 'popularity', 'revenue', 'budget']])

if __name__ == "__main__":
    main()