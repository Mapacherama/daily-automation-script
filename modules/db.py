import sqlite3
from datetime import datetime

DB_FILE = "daily_routine.db"

def create_tables():
    """Create tables for storing routine data."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hydration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                intake_ml INTEGER NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pullups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                count INTEGER NOT NULL
            )
        """)
        conn.commit()

def add_hydration(intake_ml):
    """Add hydration data to the database."""
    date = datetime.now().date()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO hydration (date, intake_ml) VALUES (?, ?)", (date, intake_ml))
        conn.commit()

def get_daily_hydration():
    """Fetch total hydration intake for today."""
    date = datetime.now().date()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(intake_ml) FROM hydration WHERE date = ?", (date,))
        result = cursor.fetchone()
        return result[0] or 0

def add_pullups(count):
    """Add pull-up data to the database."""
    date = datetime.now().date()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pullups (date, count) VALUES (?, ?)", (date, count))
        conn.commit()

def get_daily_pullups():
    """Fetch total pull-ups for today."""
    date = datetime.now().date()
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(count) FROM pullups WHERE date = ?", (date,))
        result = cursor.fetchone()
        return result[0] or 0
