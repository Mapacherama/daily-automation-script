from modules.weather import fetch_weather
from modules.news import fetch_news
from modules.todo import fetch_todo

def print_divider():
    print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    print_divider()
    print("🌤️  Today's Weather:")
    fetch_weather()

    print_divider()
    print("📰  Today's Top News:")
    fetch_news()

    print_divider()
    print("✅  To-Do List:")
    fetch_todo()

    print_divider() 