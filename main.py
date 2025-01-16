import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

from modules.news import fetch_news
from modules.todo import fetch_todo
from modules.weather import fetch_weather

load_dotenv()

def send_email(subject, body):
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("PASSWORD")
    recipient_email = sender_email  # Send to yourself

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("📧 Email sent successfully.")
    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")

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