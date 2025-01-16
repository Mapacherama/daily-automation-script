import schedule
import time
from modules.weather import fetch_weather
from modules.news import fetch_news
from modules.todo import fetch_todo

def run_morning_brief():
    print("\n===== Morning Brief =====")
    print("\n🌤️  Today's Weather:")
    fetch_weather()

    print("\n📰  Today's Top News:")
    fetch_news()

    print("\n✅  To-Do List:")
    fetch_todo()

    print("\n=========================")

# Schedule the script
schedule.every().day.at("08:00").do(run_morning_brief)

print("🕒 Morning Brief scheduled. It will run at 08:00 every day.")
while True:
    schedule.run_pending()
    time.sleep(1)