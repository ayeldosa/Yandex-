import csv
from collections import defaultdict
from datetime import datetime, timedelta
import time

user_days = defaultdict(set)

with open("input.txt", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        client_id = int(row["client_id"])
        ts = int(row["timestamp"])

        day = datetime.utcfromtimestamp(ts).date()
        user_days[client_id].add(day)

all_days = sorted({d for days in user_days.values() for d in days})

max_active = 0

for day in all_days:
    start = day - timedelta(days=29)
    active_today = 0

    for days in user_days.values():
        if day not in days:
            continue

        cnt = 0
        for d in days:
            if start <= d <= day:
                cnt += 1

        if cnt >= 5:
            active_today += 1

    max_active = max(max_active, active_today)

print(max_active)
