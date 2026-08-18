from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import (
    sum, col, avg, month, year, lag
)
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("SalesDataAnalysis") \
    .getOrCreate()

# Sample sales data
sales_data = [
    Row(date="2024-01-01", product="Laptop", price=1000, quantity=2, city="Delhi"),
    Row(date="2024-01-01", product="Mouse", price=50, quantity=5, city="Mumbai"),
    Row(date="2024-01-02", product="Laptop", price=1000, quantity=1, city="Bangalore"),

    # Additional months for MoM analysis
    Row(date="2024-02-01", product="Laptop", price=1200, quantity=2, city="Delhi"),
    Row(date="2024-02-05", product="Mouse", price=60, quantity=4, city="Mumbai"),
    Row(date="2024-02-10", product="Keyboard", price=100, quantity=3, city="Delhi"),

    Row(date="2024-03-01", product="Laptop", price=1100, quantity=3, city="Bangalore"),
    Row(date="2024-03-05", product="Mouse", price=70, quantity=6, city="Mumbai"),
    Row(date="2024-03-10", product="Keyboard", price=120, quantity=2, city="Delhi"),
]

df = spark.createDataFrame(sales_data)

print("=== Sales Data ===")
df.show()

# --------------------------------------------------
# 1. Top 5 Best-Selling Products
# --------------------------------------------------

print("=== Top 5 Best-Selling Products ===")

top_products = df.groupBy("product").agg(
    sum("quantity").alias("total_quantity")
).orderBy(
    col("total_quantity").desc()
).limit(5)

top_products.show()

# --------------------------------------------------
# 2. Month-over-Month Revenue Growth
# --------------------------------------------------

print("=== Month-over-Month Revenue Growth ===")

monthly_revenue = df.withColumn(
    "year", year("date")
).withColumn(
    "month", month("date")
).groupBy(
    "year", "month"
).agg(
    sum("price").alias("monthly_revenue")
).orderBy(
    "year", "month"
)

window_spec = Window.orderBy("year", "month")

monthly_growth = monthly_revenue.withColumn(
    "previous_revenue",
    lag("monthly_revenue").over(window_spec)
).withColumn(
    "growth_percentage",
    ((col("monthly_revenue") - col("previous_revenue"))
     / col("previous_revenue")) * 100
)

monthly_growth.show()

# --------------------------------------------------
# 3. Products with Highest Average Order Value
# --------------------------------------------------

print("=== Products with Highest Average Order Value ===")

average_order_value = df.groupBy("product").agg(
    avg("price").alias("average_order_value")
).orderBy(
    col("average_order_value").desc()
)

average_order_value.show()

# --------------------------------------------------
# Original Exercise Analysis
# --------------------------------------------------

print("=== Revenue and Quantity by Product ===")

df_grouped = df.groupBy("product").agg(
    sum("price").alias("total_revenue"),
    sum("quantity").alias("total_quantity")
)

df_grouped.show()

print("=== Revenue by City ===")

df.groupBy("city").agg(
    sum("price").alias("revenue")
).orderBy(
    col("revenue").desc()
).show()

spark.stop()
