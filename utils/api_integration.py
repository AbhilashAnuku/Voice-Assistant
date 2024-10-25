import requests
import os

class APIIntegration:
    def __init__(self):
        self.openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
        self.news_api_key = os.getenv("NEWS_API_KEY")

    def get_weather(self, city=None):
        """Get weather information for a city."""
        try:
            if city:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.openweather_api_key}&units=metric"
                response = requests.get(url)
                data = response.json()
                if response.status_code == 200:
                    return f"The weather in {city} is {data['main']['temp']}°C with {data['weather'][0]['description']}."
                else:
                    return "City not found."
            else:
                return "No city provided."
        except Exception as e:
            print(f"Error getting weather: {e}")
            return "Unable to retrieve weather."

    def get_news(self):
        """Fetch the latest news headlines from a news API."""
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={self.news_api_key}"
            response = requests.get(url)
            articles = response.json().get('articles', [])
            if articles:
                headlines = [article['title'] for article in articles]
                return "Here are the latest news headlines:\n" + "\n".join(headlines)
            return "No news found."
        except Exception as e:
            print(f"Error fetching news: {e}")
            return "Unable to retrieve news."
