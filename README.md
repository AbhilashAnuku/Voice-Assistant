# Voice Assistant

A Python voice assistant prototype for speech-driven desktop automation and information retrieval.

The assistant listens for voice commands, maps them to supported actions, and uses a collection of Python libraries and external APIs for tasks such as search, jokes, email validation, app launching, weather-style lookups, and speech feedback.

## Recruiter Notes

This project demonstrates:

- Python scripting and modular command organization
- Speech recognition and text-to-speech integration
- Environment-based API configuration
- Use of third-party APIs and automation libraries
- Early-stage assistant architecture with command, database, and utility modules

## Features

- Voice command input
- Text-to-speech responses
- Application launching helpers
- Web/API-backed information lookup
- Command modules for separating assistant behavior
- Local database support
- Environment variable support through `python-dotenv`

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- python-dotenv
- scikit-learn
- requests
- BeautifulSoup
- PyAutoGUI
- SQLite-style local persistence

## Repository Structure

```text
.
├── main.py              # Application entry point
├── commands/            # Voice command handlers
├── database/            # Local persistence helpers
├── utils/               # Shared utilities
├── requirements.txt     # Python dependencies
├── TroubleShoot.md      # Troubleshooting notes
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create a local `.env` file for any API keys required by the commands you enable:

```text
API_KEY=your_api_key_here
OTHER_API_KEY=another_api_key_here
```

Do not commit real secrets.

## Run

```bash
python main.py
```

## Notes

- Some dependencies require platform-specific setup, especially audio and automation packages.
- Microphone access is required for speech recognition.
- API-backed commands need their own credentials in `.env`.
- This is a prototype project, not a production assistant.

## Future Improvements

- Add a command registry with clear enable/disable flags
- Document which commands require which API keys
- Add tests for command parsing
- Move local runtime databases out of the repository root
