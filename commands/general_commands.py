import random

def get_general_response(query):
    """ Generate a general response based on the query. """
    responses = [
        "I'm here to assist you!",
        "What can I do for you today?",
        "How can I help you?",
        "Please tell me more!",
        "I'm listening!"
    ]
    return random.choice(responses)

def get_joke():
    """ Fetch a random joke. """
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don't scientists trust atoms? Because they make up everything!"
    ]
    return random.choice(jokes)
