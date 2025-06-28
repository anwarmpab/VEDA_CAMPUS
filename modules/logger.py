import datetime
import os

LOG_PATH = os.path.join("logs", "veda_logs.txt")

def log_interaction(source, query, response):
    os.makedirs("logs", exist_ok=True)
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{time_stamp}] ({source})\nUSER: {query}\nVEDA: {response}\n\n"

    # Fix: Open with UTF-8 encoding to support emojis
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)
