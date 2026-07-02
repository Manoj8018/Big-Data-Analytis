#!/usr/bin/env python3
import sys

max_temp = -float('inf')
hottest_date = None

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    date, temp = line.split('\t')
    temp = float(temp)

    if temp > max_temp:
        max_temp = temp
        hottest_date = date

if hottest_date is not None:
    print(f"Hottest Day: {hottest_date} with {max_temp}°C")
