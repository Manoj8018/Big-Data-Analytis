#!/usr/bin/env python3
import sys

current_product = None
total_sales = 0
product_sales = []

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    product, price = line.split('\t')
    price = float(price)

    if product == current_product:
        total_sales += price
    else:
        if current_product is not None:
            product_sales.append((total_sales, current_product))

        current_product = product
        total_sales = price

if current_product is not None:
    product_sales.append((total_sales, current_product))

product_sales.sort(reverse=True)

print("TOP 5 PRODUCTS BY SALES")
print("=" * 40)

for i, (sales, product) in enumerate(product_sales[:5], 1):
    print(f"{i}. {product}: ₹{sales:,.2f}")
