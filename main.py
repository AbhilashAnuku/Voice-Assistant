import os
import re
from dotenv import load_dotenv
from commands import (general_commands, web_commands, email_commands,
                      jokes_commands, wolfram_commands, weather_commands,
                      news_commands)
from utils.speech_recognition import SpeechRecognizer
from utils.text_to_speech import TextToSpeech
from utils.api_integration import APIIntegration
from database.database import add_data

load_dotenv()

class VoiceAssistant:
    def __init__(self):
        self.speech = TextToSpeech()
        self.recognizer = SpeechRecognizer()
        self.api = APIIntegration()

    def speak(self, text):
        """Convert text to speech and print the text."""
        print(f"Speaking: {text}")  # Print the text being spoken
        self.speech.speak(text)

    def listen(self):
        """Listen for audio input and convert it to text."""
        audio = self.recognizer.listen()
        if audio:
            try:
                command = self.recognizer.recognizer.recognize_google(audio)
                print(f"Recognized command: {command}")  # Print the command for debugging
                return command.lower()  # Normalize to lowercase
            except Exception as e:
                print(f"Error recognizing audio: {e}")
                return ""
        return ""

    def run(self):
        """Start the voice assistant."""
        self.speak("Hello, I am your voice assistant. How can I help you today?")
        while True:
            command = self.listen()
            if 'exit' in command:
                self.speak("Goodbye!")
                break
            self.main(command)

    def main(self, query):
        """Process the user's command."""
        add_data(query)  # Store command in the database
        done = False

        try:
            print(f"Processing command: {query}")  # Print the command being processed

            if ("google" in query and "search" in query) or "how to" in query:
                web_commands.googleSearch(query)
                return
            elif ("youtube" in query and "search" in query) or "play" in query:
                web_commands.youtube(query)
                return
            elif "distance" in query or "map" in query:
                web_commands.get_map(query)
                return

            # Command intents
            if "joke" in query:
                joke = jokes_commands.get_joke()
                self.speak(joke)
                done = True
            elif "news" in query:
                news = news_commands.get_news()
                self.speak(news)
                done = True
            elif "ip" in query:
                ip = web_commands.get_ip()
                self.speak(ip)
                done = True
            elif "movies" in query:
                movies = web_commands.get_popular_movies()
                self.speak("Some of the latest popular movies are:")
                self.speak(", ".join(movies))
                done = True
            elif "tv series" in query:
                tv_series = web_commands.get_popular_tvseries()
                self.speak("Some of the latest popular TV series are:")
                self.speak(", ".join(tv_series))
                done = True
            elif "weather" in query:
                city = re.search(r"(in|of|for) ([a-zA-Z]*)", query)
                if city:
                    city = city.group(2)
                    weather = weather_commands.get_weather(city)
                    self.speak(weather)
                else:
                    weather = weather_commands.get_weather()
                    self.speak(weather)
                done = True
            elif "internet speed" in query:
                self.speak("Getting your internet speed, please wait.")
                speed = web_commands.get_internet_speed(self)
                self.speak(speed)
                done = True
            # elif "system stats" in query:
            #     stats = web_commands.system_stats()
            #     self.speak(stats)
            #     done = True
            # elif "image" in query:
            #     self.speak("What kind of image do you want to generate?")
            #     text = self.recognizer.listen()
            #     self.speak("Generating image, please wait...")
            #     web_commands.generate_image(text)
            #     done = True
            elif "info" in query:
                info = web_commands.system_info()
                self.speak(info)
                done = True
            elif "send an email" in query:
                self.speak("Please provide the receiver's email ID.")
                receiver_id = input("Enter receiver's email ID: ")
                while not email_commands.check_email(receiver_id):
                    self.speak("Invalid email ID. Please provide it again.")
                    receiver_id = input("Enter receiver's email ID: ")

                subject = input("Enter the subject of the email: ")  # Prompt for subject
                body = input("Enter the message body of the email: ")  # Prompt for body

                success = email_commands.send_email(receiver_id, subject, body)
                if success:
                    self.speak("Email sent successfully.")
                else:
                    self.speak("There was an error sending the email.")
                done = True
            elif "note" in query:
                self.speak("What would you like to take down?")
                audio_note = self.recognizer.listen()  # Get audio input
                try:
                    # Convert audio to text
                    note = self.recognizer.recognizer.recognize_google(audio_note)
                    web_commands.take_note(note)  # Save the note
                    self.speak(f"Note saved: {note}")  # Confirm saving the note
                except Exception as e:
                    self.speak("Sorry, I could not understand the note.")
                    print(f"Error: {e}")
                done = True
            elif "wikipedia" in query:
                description = wolfram_commands.tell_me_about(query)
                self.speak(description)
                done = True
            elif "open" in query:
                completed = web_commands.open_specified_website(query)
                if completed:
                    done = True
            elif "app" in query:
                completed = web_commands.open_app(query)
                if completed:
                    done = True

            # Default response
            if not done:
                answer = general_commands.get_general_response(query)
                self.speak(answer)

        except Exception as e:
            self.speak(f"An error occurred: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
