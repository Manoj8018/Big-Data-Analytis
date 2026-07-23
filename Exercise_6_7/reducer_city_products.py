#!/usr/bin/env python3
import sys

current_key = None
total_sales = 0
results = {}

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    key, price = line.split('\t')
    price = float(price)

    if key == current_key:
        total_sales += price
    else:
        if current_key is not None:
            city, product = current_key.split('_')
            if city not in results:
                results[city] = []
            results[city].append((total_sales, product))

        current_key = key
        total_sales = price

if current_key is not None:
    city, product = current_key.split('_')
    if city not in results:
        results[city] = []
    results[city].append((total_sales, product))

print("TOP PRODUCT PER CITY:")
print("=" * 40)

for city, products in results.items():
    products.sort(reverse=True)
    top_product = products[0]
    print(f"{city}: {top_product[1]} (₹{top_product[0]:,.2f})")
