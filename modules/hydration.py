import sqlite3
from datetime import date

DB_FILE = "hydration.db"

def create_hydration_table():
    """Create the hydration table if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hydration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL UNIQUE,
                intake_ml INTEGER NOT NULL
            )
        """)
        conn.commit()

def get_hydration_data():
    """Retrieve today's hydration data or initialize it."""
    today = str(date.today())
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT intake_ml FROM hydration WHERE date = ?", (today,))
        result = cursor.fetchone()
        if result:
            return {"date": today, "intake_ml": result[0]}
        else:
            # Initialize data for today
            cursor.execute("INSERT INTO hydration (date, intake_ml) VALUES (?, ?)", (today, 0))
            conn.commit()
            return {"date": today, "intake_ml": 0}

def save_hydration_data(data):
    """Update hydration data in the database."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE hydration SET intake_ml = ? WHERE date = ?", (data["intake_ml"], data["date"]))
        conn.commit()