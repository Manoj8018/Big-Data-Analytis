from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

spark = SparkSession.builder \
    .appName("LogAnalysis") \
    .getOrCreate()

# Read log file
df = spark.read.text("access.log")

print("=== Raw Logs ===")
df.show(truncate=False)

# Extract IP address
logs = df.select(
    col("value").alias("log")
)

ip_df = logs.select(
    logs.log.substr(1, 12).alias("ip")
)

print("=== Requests by IP ===")
ip_df.groupBy("ip") \
    .count() \
    .orderBy(col("count").desc()) \
    .show()

# Count successful requests
success_count = df.filter(
    col("value").contains(" 200")
).count()

print("=== Successful Requests ===")
print(success_count)

# Count error requests
error_count = df.filter(
    col("value").rlike(r" (4\d\d|5\d\d)$")
).count()

print("=== Error Requests ===")
print(error_count)

# Count requests by status code
status_df = df.selectExpr(
    "regexp_extract(value, ' (\\\\d{3})$', 1) as status"
)

print("=== Requests by Status Code ===")
status_df.groupBy("status") \
    .count() \
    .orderBy("status") \
    .show()

spark.stop()
