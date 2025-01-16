def fetch_todo():
    todo_items = [
        "🚀 Work on Python automation script",
        "🏋️ Hit the gym",
        "📚 Read 20 pages of 'Der Name des Windes'",
        "☕ Enjoy a great coffee break"
    ]

    print("\nToday's To-Do List:")
    for idx, item in enumerate(todo_items, start=1):
        print(f"{idx}. {item}")