#!/usr/bin/env python3

import sys
from collections import defaultdict

current_date = None
users = set()
songs = defaultdict(int)
artists = defaultdict(int)

total_duration = 0
total_plays = 0


def output():
    if current_date is None:
        return

    top_song = max(songs, key=songs.get)
    top_artist = max(artists, key=artists.get)

    avg_duration = total_duration / total_plays if total_plays else 0

    print(
        f"{current_date}\t{total_plays}\t{len(users)}\t"
        f"{avg_duration:.2f}\t{top_song}\t{top_artist}"
    )


for line in sys.stdin:

    date, value = line.strip().split("\t")
    user_id, song, artist, duration = value.split(",")

    duration = float(duration)

    if current_date is None:
        current_date = date

    if date != current_date:
        output()

        current_date = date
        users = set()
        songs = defaultdict(int)
        artists = defaultdict(int)
        total_duration = 0
        total_plays = 0

    users.add(user_id)
    songs[song] += 1
    artists[artist] += 1
    total_duration += duration
    total_plays += 1

output()
