import requests

def get_daily_quote():
    """Fetch a daily motivational quote from an API and return it."""
    try:
        response = requests.get("https://type.fit/api/quotes")  # Replace with the API you're using
        response.raise_for_status()  # Raise an exception for HTTP errors
        quotes = response.json()

        # Pick a random quote from the list
        import random
        random_quote = random.choice(quotes)

        return random_quote['text'] + " - " + random_quote['author'] if random_quote['author'] else random_quote['text']
    except requests.exceptions.RequestException as e:
        # Handle connection errors or API failures
        return "Stay positive and keep moving forward! (Couldn't fetch a fresh quote today.)"