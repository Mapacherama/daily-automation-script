import requests
from bs4 import BeautifulSoup

def fetch_weather():
    url = "https://wttr.in?format=3"  # Quick weather API
    response = requests.get(url)
    print(f"Today's Weather: {response.text}")

if __name__ == "__main__":
    fetch_weather()