from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

spark = SparkSession.builder \
    .appName("SparkOptimization") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Sample sales data
data = [
    (1, "Laptop", "Delhi", 60000),
    (2, "Mouse", "Mumbai", 1500),
    (3, "Laptop", "Delhi", 55000),
    (4, "Keyboard", "Bangalore", 3000),
    (5, "Monitor", "Delhi", 15000),
    (6, "Mouse", "Mumbai", 2000),
    (7, "Laptop", "Bangalore", 58000),
    (8, "Keyboard", "Delhi", 3500),
    (9, "Monitor", "Mumbai", 16000),
    (10, "Laptop", "Delhi", 62000)
]

df = spark.createDataFrame(
    data,
    ["order_id", "product", "city", "amount"]
)

print("=== Original Data ===")
df.show()

# -----------------------------------
# 1. Filter early
# -----------------------------------

filtered = df.filter(col("amount") > 10000)

print("=== Orders Above 10000 ===")
filtered.show()

# -----------------------------------
# 2. Select only required columns
# -----------------------------------

selected = filtered.select(
    "product",
    "city",
    "amount"
)

print("=== Selected Columns ===")
selected.show()

# -----------------------------------
# 3. Aggregation
# -----------------------------------

revenue = selected.groupBy("product").agg(
    sum("amount").alias("total_revenue")
)

print("=== Revenue by Product ===")
revenue.orderBy(
    col("total_revenue").desc()
).show()

# -----------------------------------
# 4. Cache frequently used DataFrame
# -----------------------------------

filtered.cache()

print("Cached partitions:", filtered.rdd.getNumPartitions())

# Force cache materialization
filtered.count()

print("=== Cached Data ===")
filtered.show()

# -----------------------------------
# 5. Explain execution plan
# -----------------------------------

print("=== Optimized Execution Plan ===")

revenue.explain("formatted")

spark.stop()
