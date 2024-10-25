import requests
import os

def get_general_response(query):
    """Fetch general responses using Wolfram Alpha API."""
    api_key = os.getenv('WOLFRAM_API_KEY')
    try:
        url = f"http://api.wolframalpha.com/v2/query?input={query}&format=plaintext&output=JSON&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        pods = data['queryresult']['pods']
        if pods:
            return pods[0]['subpods'][0]['plaintext']
        return "No information found."
    except Exception as e:
        print(f"Error fetching information: {e}")
        return "Unable to retrieve information."
