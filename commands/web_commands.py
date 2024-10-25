import webbrowser
import requests
import re
import os
import platform
import psutil

def take_note(note):
    """Save a note to a text file."""
    notes_file = "notes.txt"
    with open(notes_file, "a") as file:
        file.write(note + "\n")
    return f"Note saved: {note}"

def googleSearch(query):
    """ Perform a Google search. """
    search_query = query.replace("google search", "").strip()
    url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(url)

def youtube(query):
    """ Search on YouTube. """
    search_query = query.replace("youtube search", "").strip()
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)

def get_map(query):
    """ Get directions using Google Maps. """
    location = query.replace("map", "").strip()
    url = f"https://www.google.com/maps/search/?api=1&query={location}"
    webbrowser.open(url)

def get_ip():
    """ Get the public IP address. """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        print(f"Error getting IP: {e}")
        return "Unable to retrieve IP."

def get_weather(city=None, api_key="YOUR_OPENWEATHER_API_KEY"):
    """ Get weather information for a city using OpenWeatherMap API. """
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

def open_specified_website(query):
    """ Open a specified website based on the query. """
    website = query.replace("open", "").strip()
    url = f"http://{website}" if not website.startswith("http") else website
    webbrowser.open(url)

import subprocess
def open_app(query):
    """ Open a specified application. """
    app_name = query.replace("open", "").strip()
    app_paths = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe"
    }
    app_path = app_paths.get(app_name.lower())
    if app_path:
        subprocess.Popen(app_path)
        return True
    return False

def system_info():
    """Return basic system information."""
    info = f"System: {platform.system()}\n"
    info += f"Node Name: {platform.node()}\n"
    info += f"Release: {platform.release()}\n"
    info += f"Version: {platform.version()}\n"
    info += f"Machine: {platform.machine()}\n"
    info += f"Processor: {platform.processor()}\n"
    
    # Memory info
    mem = psutil.virtual_memory()
    info += f"Total Memory: {mem.total / (1024 ** 3):.2f} GB\n"
    info += f"Available Memory: {mem.available / (1024 ** 3):.2f} GB\n"
    
    return info

import requests
import os

def get_popular_movies():
    """Fetch and return the latest popular movies."""
    api_key = os.getenv('TMDB_API_KEY')  # Add your TMDB API key to the .env file
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        movies = response.json().get('results', [])
        
        if not movies:
            return ["No popular movies found."]
        
        return [movie['title'] for movie in movies]
    
    except Exception as e:
        print(f"Error fetching popular movies: {e}")
        return ["Error fetching movies."]

def get_popular_tvseries():
    """Fetch and return the latest popular TV series."""
    api_key = os.getenv('TMDB_API_KEY')  
    url = f"https://api.themoviedb.org/3/tv/popular?api_key={api_key}&language=en-US&page=1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        tv_series = response.json().get('results', [])
        
        if not tv_series:
            return ["No popular TV series found."]
        
        return [series['name'] for series in tv_series]
    
    except Exception as e:
        print(f"Error fetching popular TV series: {e}")
        return ["Error fetching TV series."]


import speedtest
import requests

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def get_speedtest_results():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    st.results.share()
    return st.results.dict()

def get_internet_speed(voice_assistant):
    if check_internet_connection():
        voice_assistant.speak("Getting your internet speed, please wait.")
        try:
            speed_results = get_speedtest_results()
            download_speed = speed_results['download'] / 1_000_000  
            upload_speed = speed_results['upload'] / 1_000_000  
            ping = speed_results['ping']

            result_message = (
                f"Download speed: {download_speed:.2f} Mbps. "
                f"Upload speed: {upload_speed:.2f} Mbps. "
                f"Ping: {ping} ms."
            )
            voice_assistant.speak(result_message)
        except Exception as e:
            voice_assistant.speak(f"An error occurred while performing the speed test: {e}")
    else:
        voice_assistant.speak("It looks like you are not connected to the internet.")

