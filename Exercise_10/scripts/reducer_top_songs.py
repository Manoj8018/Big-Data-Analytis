#!/usr/bin/env python3

import sys
from collections import defaultdict

current_date = None
song_counts = defaultdict(int)

def output():
    if current_date is None:
        return

    sorted_songs = sorted(
        song_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for rank, (song, count) in enumerate(sorted_songs[:10], start=1):
        print(f"{current_date}\t{rank}\t{song}\t{count}")

for line in sys.stdin:
    date, song = line.strip().split("\t")

    if current_date is None:
        current_date = date

    if date != current_date:
        output()
        current_date = date
        song_counts = defaultdict(int)

    song_counts[song] += 1

output()
