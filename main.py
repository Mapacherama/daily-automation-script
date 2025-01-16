import requests
from bs4 import BeautifulSoup

def fetch_weather():
    url = "https://wttr.in?format=3"  # Quick weather API
    response = requests.get(url)
    print(f"Today's Weather: {response.text}")

import requests
import feedparser

def fetch_news():
    url = "https://news.google.com/rss"  # Google News RSS Feed
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Fetch the RSS feed
    response = requests.get(url, headers=headers)

    # Check if response is successful
    if response.status_code != 200:
        print("⚠️ Failed to fetch news. Please check the RSS feed URL or your internet connection.")
        return

    # Parse the RSS feed
    feed = feedparser.parse(response.content)

    print("\nToday's Top News:")
    for idx, entry in enumerate(feed.entries[:5], start=1):  # Top 5 headlines
        print(f"{idx}. {entry.title} - {entry.link}")

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