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
        product = parts[1]
        price = float(parts[2])
        city = parts[3]
        customer = parts[4]
        quantity = int(parts[5])

        total = price * quantity

        print(f"{city}\t{total}")

    except ValueError:
        continue
