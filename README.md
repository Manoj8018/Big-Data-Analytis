# Big Data Analytics - Hadoop Streaming MapReduce Exercises

# Project Overview

This repository contains Hadoop Streaming MapReduce programs developed as part of the **Big Data Analytics** laboratory. The exercises demonstrate how Python can be used as Mapper and Reducer programs with Hadoop Streaming to process large datasets stored in HDFS.

---

## Technologies Used

- Hadoop 3.4.2
- HDFS
- YARN
- Hadoop Streaming
- Python 3
- Ubuntu (WSL)
- Git & GitHub

---

## Project Structure

Big-Data-Analytis/

│── mapper_max_temp.py
│── reducer_max_temp.py
│── reducer_min_temp.py
│── mapper_top_products.py
│── reducer_top_products.py
│── mapper_city_products.py
│── reducer_city_products.py
│── weather_data.txt
│── weather_large.txt
│── sales_products.txt
│── sales_products_large.txt
│── README.md


---

# Exercise 1 - Weather Data Analysis

### Objective

Find:

- Hottest Day
- Coldest Day

using Hadoop Streaming MapReduce.

### Dataset Format

Date,City,MaxTemp,MinTemp
024-01-01,Delhi,12,5

### Mapper Output

2024-01-01 12
2024-01-02 14


### Expected Output

Hottest Day: 2024-01-09 with 33.0°C

Coldest Day: 2024-01-03 with 10.0°C



---

# Exercise 2 - Sales Analysis

### Objective

Find:

- Top 5 Products by Sales
- Top Product in Each City

### Dataset Format
Date,Product,Price,City
2024-01-01,Laptop,45000,Delhi


### Expected Output
TOP 5 PRODUCTS BY SALES

Laptop
Monitor
Keyboard
Mouse


### City-wise Output
TOP PRODUCT PER CITY

Delhi : Laptop
Mumbai : Monitor
Bangalore : Laptop
Chennai : Laptop



