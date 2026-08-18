from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, sum, avg, row_number
)
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("ETLPipeline") \
    .getOrCreate()

# ---------------------------------------
# 1. Extract
# ---------------------------------------

customers = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("customers.csv")

orders = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("orders.csv")

print("=== Customers ===")
customers.show()

print("=== Orders ===")
orders.show()

# ---------------------------------------
# 2. Transform
# ---------------------------------------

# Join customers and orders
joined = orders.join(
    customers,
    orders.customer_id == customers.customer_id,
    "inner"
)

print("=== Joined Data ===")
joined.select(
    orders.order_id,
    customers.name,
    customers.city,
    orders.product,
    orders.amount,
    orders.order_date
).show()

# ---------------------------------------
# 3. Aggregation
# ---------------------------------------

city_revenue = joined.groupBy("city").agg(
    sum("amount").alias("total_revenue"),
    avg("amount").alias("average_order_value")
).orderBy(
    col("total_revenue").desc()
)

print("=== Revenue by City ===")
city_revenue.show()

# ---------------------------------------
# 4. Window Function
# ---------------------------------------

window_spec = Window.partitionBy("city") \
    .orderBy(col("amount").desc())

ranked_orders = joined.withColumn(
    "order_rank",
    row_number().over(window_spec)
)

print("=== Ranked Orders by City ===")

ranked_orders.select(
    "city",
    "name",
    "product",
    "amount",
    "order_rank"
).orderBy(
    "city",
    "order_rank"
).show()

# ---------------------------------------
# 5. Load
# ---------------------------------------

city_revenue.write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/city_revenue")

print("ETL pipeline completed successfully.")

spark.stop()
