# Exercise 5 – Hadoop Streaming Sales Data Analysis

## Objective

The objective of this exercise is to perform sales data analysis using Hadoop Streaming and Python MapReduce programs.

## Files Included

- generate_sales.py – Generates sample sales data.
- mapper_city_sales.py – Calculates total sales for each city.
- reducer_city_sales.py – Reduces city-wise sales data.
- mapper_monthly_sales.py – Calculates monthly sales.
- reducer_monthly_sales.py – Reduces monthly sales data.
- mapper_product_qty.py – Calculates product quantities sold.
- reducer_product_qty.py – Reduces product quantity data.
- visualize_sales.py – Generates visualizations from the analysis.
- sales.csv – Sample sales dataset.
- sales_analysis.png – Visualization of the analysis.

## Requirements

- Ubuntu (WSL/Linux)
- Python 3
- Hadoop 3.x
- Hadoop Streaming

## Execution Steps

### Generate the dataset

```bash
python3 generate_sales.py
```

### Run City-wise Sales Analysis

```bash
cat sales.csv | python3 mapper_city_sales.py | sort | python3 reducer_city_sales.py
```

### Run Monthly Sales Analysis

```bash
cat sales.csv | python3 mapper_monthly_sales.py | sort | python3 reducer_monthly_sales.py
```

### Run Product Quantity Analysis

```bash
cat sales.csv | python3 mapper_product_qty.py | sort | python3 reducer_product_qty.py
```

### Generate Visualization

```bash
python3 visualize_sales.py
```

## Output

- City-wise total sales
- Monthly sales summary
- Product quantity summary
- Sales visualization (`sales_analysis.png`)


