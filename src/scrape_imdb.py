import requests
import json
import pandas as pd

def scrape_top_100_movies():
    url = "https://www.imdb.com/chart/top/"
    headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return

    text = response.text

    # Extract the JSON-LD part from the page
    start = text.find('<script type="application/ld+json">')
    if start == -1:
        print("JSON-LD script tag not found")
        return
    start += len('<script type="application/ld+json">')
    end = text.find('</script>', start)
    json_str = text[start:end].strip()

    # Parse the JSON-LD
    data = json.loads(json_str)

    movies_data = data.get('itemListElement', [])[:100]

    movies = []
    for item in movies_data:
        movie = item['item']
        movies.append({
            'title': movie.get('name'),
            'year': int(movie.get('url').split('/title/')[1][:7].split('/')[0][-4:]) if 'url' in movie else None,  # fallback
            'rating': float(movie.get('aggregateRating', {}).get('ratingValue', 0)),
            'link': movie.get('url'),
            'description': movie.get('description')
        })

    df = pd.DataFrame(movies)
    df.to_csv("data/imdb_raw.csv", index=False)
    print("✅ Scraped and saved top 100 movies to data/imdb_raw.csv")

if __name__ == "__main__":
    scrape_top_100_movies()
