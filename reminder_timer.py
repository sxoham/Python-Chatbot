import threading
import time

def set_reminder(message, seconds, callback=None):
    def reminder_task():
        time.sleep(seconds)
        response = f"⏰ Reminder: {message}"
        print(response)
        if callback:
            callback("Bot", response)
    threading.Thread(target=reminder_task).start()
    return f"✅ Reminder set for {seconds // 60} minutes and {seconds % 60} seconds."
