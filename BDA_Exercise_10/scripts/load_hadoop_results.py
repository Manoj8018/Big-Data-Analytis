#!/usr/bin/env python3

from cassandra.cluster import Cluster
from datetime import datetime
from pathlib import Path

cluster = Cluster(["localhost"])
session = cluster.connect("streaming_analytics")

output_file = (
    Path.home()
    / "hadoop-cassandra-exercise"
    / "output"
    / "daily_aggregates.txt"
)

print("Loading Hadoop results into Cassandra...")

count = 0

with open(output_file) as f:
    for line in f:
        if not line.strip():
            continue

        parts = line.strip().split("\t")

        if len(parts) != 6:
            continue

        date, plays, users, avg, song, artist = parts

        session.execute(
            """
            INSERT INTO daily_aggregates
            (date,total_plays,unique_users,avg_duration,top_song,top_artist)
            VALUES (%s,%s,%s,%s,%s,%s)
            """,
            (
                datetime.strptime(date, "%Y-%m-%d").date(),
                int(plays),
                int(users),
                float(avg),
                song,
                artist,
            ),
        )

        count += 1

print(f"{count} records inserted.")

cluster.shutdown()
