import schedule
import time
from modules.weather import fetch_weather
from modules.news import fetch_news
from modules.todo import fetch_todo

from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Morning Brief",
        timeout=10  # Notification duration (seconds)
    )

def run_morning_brief():
    # Prepare brief as a single message
    weather = "🌤️ Weather:\n" + fetch_weather()
    news = "📰 News:\n" + "\n".join([f"{idx+1}. {headline}" for idx, headline in enumerate(fetch_news())])
    todo = "✅ To-Do:\n" + "\n".join(fetch_todo())

    # Display in the terminal
    print("\n===== Morning Brief =====")
    print(weather)
    print(news)
    print(todo)
    print("\n=========================")

    # Send as a notification
    send_notification("Morning Brief", f"{weather}\n\n{news}\n\n{todo}")

# Schedule the script
schedule.every().day.at("08:00").do(run_morning_brief)

print("🕒 Morning Brief scheduled. It will run at 08:00 every day.")
while True:
    schedule.run_pending()
    time.sleep(1)