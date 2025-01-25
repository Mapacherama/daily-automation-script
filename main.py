from flask import Flask, jsonify, request
from modules.hydration import get_hydration_data
from modules.news import fetch_news
from modules.todo import fetch_todo
from modules.weather import fetch_weather
from modules.email import send_email
from modules.db import create_tables

import schedule
# Initialize Flask app
app = Flask(__name__)

# Initialize database
create_tables()

# Endpoint to fetch weather data
@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        weather = fetch_weather()
        return jsonify({"weather": weather, "status": "success"}), 200
    except ConnectionError:
        return jsonify({
            "error": "Failed to connect to weather service",
            "status": "error"
        }), 503
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

# Endpoint to fetch news headlines
@app.route('/news', methods=['GET'])
def get_news():
    news = fetch_news()
    return jsonify({"news": news})

# Endpoint to fetch to-do items
@app.route('/todo', methods=['GET'])
def get_todo():
    todo = fetch_todo()
    return jsonify({"todo": todo})

# Endpoint to fetch hydration data
@app.route('/hydration', methods=['GET'])
def get_hydration():
    hydration_data = get_hydration_data()
    return jsonify({"hydration": hydration_data})

# Endpoint to send morning brief
@app.route('/send-brief', methods=['POST'])
def send_brief():
    weather = "🌤️ Weather:\n" + fetch_weather()
    news = "📰 News:\n" + "\n".join([f"{idx+1}. {headline}" for idx, headline in enumerate(fetch_news())])
    todo = "✅ To-Do:\n" + "\n".join(fetch_todo())

    hydration_data = get_hydration_data()
    hydration_status = f"💧 Hydration:\nTotal intake: {hydration_data['intake_ml']} ml."

    # Prepare and send brief
    brief = f"{weather}\n\n{news}\n\n{todo}\n\n{hydration_status}"
    print("\n===== Morning Brief =====")
    print(brief)
    print("=========================")
    send_email("Morning Brief", brief)

    return jsonify({"message": "Morning brief sent!", "brief": brief})

# Endpoint to schedule morning brief (optional, cron jobs are better for production)
@app.route('/schedule-brief', methods=['POST'])
def schedule_brief():
    schedule_time = request.json.get('schedule_time', '07:00')
    schedule.every().day.at(schedule_time).do(run_morning_brief)

    # Run scheduling loop in a separate thread or background process (not recommended for production)
    # For production, use a task scheduler like Celery + Redis.
    return jsonify({"message": f"Morning brief scheduled daily at {schedule_time}!"})

def run_morning_brief():
    # Prepare brief
    weather = "🌤️ Weather:\n" + fetch_weather()
    news = "📰 News:\n" + "\n".join([f"{idx+1}. {headline}" for idx, headline in enumerate(fetch_news())])
    todo = "✅ To-Do:\n" + "\n".join(fetch_todo())

    hydration_data = get_hydration_data()
    hydration_status = f"💧 Hydration:\nTotal intake: {hydration_data['intake_ml']} ml."

    # Prepare and send brief
    brief = f"{weather}\n\n{news}\n\n{todo}\n\n{hydration_status}"
    print("\n===== Morning Brief =====")
    print(brief)
    print("=========================")
    send_email("Morning Brief", brief)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)