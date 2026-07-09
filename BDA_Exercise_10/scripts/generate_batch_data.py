#!/usr/bin/env python3

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

artists = [
    "The Beatles", "Led Zeppelin", "Pink Floyd", "Queen",
    "Nirvana", "Michael Jackson", "Madonna", "U2",
    "Eagles", "AC/DC"
]

songs = [
    "Hey Jude", "Stairway to Heaven", "Comfortably Numb",
    "Bohemian Rhapsody", "Smells Like Teen Spirit",
    "Billie Jean", "Like a Prayer", "With or Without You",
    "Hotel California", "Back in Black"
]

output_file = Path.home() / "hadoop-cassandra-exercise" / "data" / "batch_plays.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "user_id",
        "timestamp",
        "song",
        "artist",
        "session_id",
        "duration"
    ])

    start_date = datetime(2024, 1, 1)

    for _ in range(10000):
        user_id = random.randint(1, 1000)
        date = start_date + timedelta(days=random.randint(0, 730))
        timestamp = date + timedelta(
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        writer.writerow([
            user_id,
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            random.choice(songs),
            random.choice(artists),
            random.randint(1000, 9999),
            round(random.uniform(2.5, 10.0), 2)
        ])

print(f"Generated: {output_file}")
print("Records: 10000")
