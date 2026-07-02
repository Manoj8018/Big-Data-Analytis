#!/usr/bin/env python3
import sys

current_city = None
total_sales = 0
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    city, amount = line.split('\t')
    amount = float(amount)

    if city == current_city:
        total_sales += amount
        count += 1
    else:
        if current_city is not None:
            print(f"{current_city}\t{total_sales:.2f}\t{count}")

        current_city = city
        total_sales = amount
        count = 1

if current_city is not None:
    print(f"{current_city}\t{total_sales:.2f}\t{count}")
