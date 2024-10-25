import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

# Create or connect to a SQLite database
DATABASE_NAME = os.getenv("DATABASE_NAME", "voice_assistant.db")

def create_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table():
    """Create a table for storing commands."""
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT NOT NULL
            )
        ''')
    conn.close()

def add_data(command):
    """Insert a new command into the commands table."""
    conn = create_connection()
    with conn:
        conn.execute('''
            INSERT INTO commands (command)
            VALUES (?)
        ''', (command,))
    conn.close()

# Create the table if it doesn't exist
create_table()
