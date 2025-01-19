from plyer import notification

import schedule
import time

def schedule_hydration_reminders():
    schedule.every(2).hours.do(remind_hydration)  # Remind every 2 hours
    print("⏰ Hydration reminders scheduled every 2 hours.")
    while True:
        schedule.run_pending()
        time.sleep(1)

def remind_hydration():
    title = "💧 Hydration Reminder"
    message = "It's time to drink some water and stay hydrated!"
    notification.notify(
        title=title,
        message=message,
        app_name="Personal Assistant",
        timeout=10  # Notification disappears after 10 seconds
    )
    print("💧 Reminder: Time to hydrate! Notification sent.")
