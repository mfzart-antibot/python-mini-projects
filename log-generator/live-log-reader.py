"""
Terminal activated script that reads the given LOG file and prints alert if too many errors within last 60Sec
"""

import sys
import json
import time
from collections import deque

if len(sys.argv) < 3:
    print("Usage: python live-log-reader.py <log_file> <ERROR_THRESHOLD>")
    sys.exit()

log_file = sys.argv[1]

THRESHOLD = int(sys.argv[2])  # ile ERRORÓW
WINDOW_SEC = 60  # ... w jakim oknie czasowym (sekundy)
COOLDOWN = 30  # co ile sekund max powtórzyć alert

error_times = deque()  # tu trzymam czas wystąpień ERROR
last_alert_time = 0

with open(log_file, "r") as f:

    f.seek(0, 2)  # na koniec pliku

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        line = line.strip()
        print(line)

        now = time.time()  # jeśli to error, zapisz czas wystąpienia
        if "ERROR" in line:
            error_times.append(now)
            # zrzucanie ERROROw do zewnetrznego JSONa
            event = {"timestamp": now, "message": line}
            with open("errors.json", "a") as file:
                file.write(json.dumps(event) + "\n")

        # usuń stare ERRORy spoza okna czasu (starsze niż WINDOW_SEC)
        while error_times and (now - error_times[0] > WINDOW_SEC):
            error_times.popleft()

        # policz ERRORy w oknie
        errors_in_window = len(error_times)

        # ALERT: tylko jeśli przekroczono próg i minął cooldown
        if errors_in_window >= THRESHOLD and (now - last_alert_time) >= COOLDOWN:
            print(f"ALERT: {errors_in_window} ERROR in last {WINDOW_SEC}s")
            last_alert_time = now
