import threading
import time
import os
from playsound import playsound
from datetime import datetime

def set_alarm(alarm_time_str, callback=None):
    def alarm_task():
        while True:
            current_time = datetime.now().strftime("%H:%M")
            if current_time == alarm_time_str:
                file_path = os.path.abspath("alarm.mp3")
                print(f"🔊 Playing sound from: {file_path}")
                try:
                    playsound(file_path)
                except Exception as e:
                    print(" Sound failed:", e)
                if callback:
                    callback("Bot", f" Alarm ringing at {alarm_time_str}!")
                break
            time.sleep(30)
    threading.Thread(target=alarm_task).start()
    return f" Alarm set for {alarm_time_str}"

