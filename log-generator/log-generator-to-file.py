"""Log Generator
Randomly produce LOGs and saves them to file
"""

import random
import time
from datetime import datetime

LOG_MESSAGES = {
    "INFO": [
        "User Login Successful",
        "Background job started",
        "File uploaded successfully",
    ],
    "WARNING": [
        "Disk usage high",
        "API response slow",
        "Memory usage increased",
    ],
    "ERROR": [
        "Database connection failed",
        "Timeout while contacting service",
        "File not found",
    ],
}


def log_stream():
    level = random.choice(list(LOG_MESSAGES.keys()))
    message = random.choice(LOG_MESSAGES[level])
    event_id = random.randint(1000, 9999)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} | {level} | Event #{event_id} | {message}"


def save_logs_to_file(filename="system.log", interval=0.5):
    while True:
        log_line = log_stream()
        with open("system.log", "a", encoding="utf-8") as f:  # Saving logs to file
            f.write(log_line + "\n")
        time.sleep(interval)


save_logs_to_file()
