from plyer import notification

import schedule
import time

import json
from datetime import date

HYDRATION_FILE = "hydration.json"

def get_hydration_data():
    try:
        with open(HYDRATION_FILE, "r") as file:
            data = json.load(file)
        if data["date"] != str(date.today()):
            data = {"date": str(date.today()), "intake_ml": 0}  # Reset for a new day
            save_hydration_data(data)
        return data
    except FileNotFoundError:
        data = {"date": str(date.today()), "intake_ml": 0}
        save_hydration_data(data)
        return data

def save_hydration_data(data):
    with open(HYDRATION_FILE, "w") as file:
        json.dump(data, file)

def schedule_hydration_reminders():
    schedule.every(2).hours.do(remind_hydration)  # Remind every 2 hours
    print("⏰ Hydration reminders scheduled every 2 hours.")
    while True:
        schedule.run_pending()
        time.sleep(1)

def remind_hydration():
    title = "💧 Hydration Reminder"
    message = "It's time to drink some water and stay hydrated!"
    notification.notify(
        title=title,
        message=message,
        app_name="Personal Assistant",
        timeout=10  # Notification disappears after 10 seconds
    )
    print("💧 Reminder: Time to hydrate! Notification sent.")

def calculate_hydration(weight_kg, active_hours):
    base = weight_kg * 30  # 30 ml per kg body weight
    additional = active_hours * 350  # 350 ml per hour of activity
    return base + additional
