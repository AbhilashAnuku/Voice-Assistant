import requests
import os

def get_news():
    """Fetch the latest news headlines from a news API."""
    api_key = os.getenv("NEWS_API_KEY")
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        articles = response.json().get('articles', [])
        if articles:
            headlines = [article['title'] for article in articles]
            return "Here are the latest news headlines:\n" + "\n".join(headlines)
        return "No news found."
    except Exception as e:
        print(f"Error fetching news: {e}")
        return "Unable to retrieve news."
