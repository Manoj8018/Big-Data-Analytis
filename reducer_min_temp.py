#!/usr/bin/env python3
import sys

min_temp = float('inf')
coldest_date = None

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    date, temp = line.split('\t')
    temp = float(temp)

    if temp < min_temp:
        min_temp = temp
        coldest_date = date

if coldest_date is not None:
    print(f"Coldest Day: {coldest_date} with {min_temp}°C")
