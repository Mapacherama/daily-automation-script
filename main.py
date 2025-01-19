import os

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

    # Print brief
    print("\n===== Morning Brief =====")
    print(weather)
    print(news)
    print(todo)
    print("\n=========================")

    # Send email
    send_email("Morning Brief", f"{weather}\n\n{news}\n\n{todo}")