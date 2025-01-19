import os

from modules.hydration import get_hydration_data
from modules.news import fetch_news
from modules.todo import fetch_todo
from modules.weather import fetch_weather
from modules.email import send_email

import schedule
import time

def schedule_brief():
    schedule_time = os.getenv("SCHEDULE_TIME", "07:00")
    schedule.every().day.at(schedule_time).do(run_morning_brief)
    while True:
        schedule.run_pending()
        time.sleep(1)

def run_morning_brief():
    # Prepare brief
    weather = "🌤️ Weather:\n" + fetch_weather()
    news = "📰 News:\n" + "\n".join([f"{idx+1}. {headline}" for idx, headline in enumerate(fetch_news())])
    todo = "✅ To-Do:\n" + "\n".join(fetch_todo())

    hydration_data = get_hydration_data()
    hydration_status = f"💧 Hydration:\nTotal intake: {hydration_data['intake_ml']} ml."

    schedule_brief()
    
    # Prepare and send brief
    brief = f"{weather}\n\n{news}\n\n{todo}\n\n{hydration_status}"
    print("\n===== Morning Brief =====")
    print(brief)
    print("=========================")
    send_email("Morning Brief", brief)

