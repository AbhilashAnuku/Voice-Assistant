import requests
import os

def get_weather(city=None):
    """Get weather information for a city using OpenWeatherMap API."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    try:
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
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
