#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split(',')

    if len(parts) != 6:
        continue

    try:
        date = parts[0]
        month = date[:7]
        price = float(parts[2])
        quantity = int(parts[5])

        total = price * quantity

        print(f"{month}\t{total}")

    except ValueError:
        continue
