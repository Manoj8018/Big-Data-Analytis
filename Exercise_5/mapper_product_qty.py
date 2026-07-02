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
        product = parts[1]
        quantity = int(parts[5])

        print(f"{product}\t{quantity}")

    except ValueError:
        continue
