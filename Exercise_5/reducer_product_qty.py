#!/usr/bin/env python3
import sys

current_product = None
total_qty = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    product, qty = line.split('\t')
    qty = int(qty)

    if product == current_product:
        total_qty += qty
    else:
        if current_product is not None:
            print(f"{current_product}\t{total_qty}")

        current_product = product
        total_qty = qty

if current_product is not None:
    print(f"{current_product}\t{total_qty}")
