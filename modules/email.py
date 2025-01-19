from email.mime.text import MIMEText
import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body):
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("PASSWORD")
    recipient_email = sender_email

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