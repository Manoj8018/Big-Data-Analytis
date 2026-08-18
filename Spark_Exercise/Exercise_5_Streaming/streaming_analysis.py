from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, window

spark = SparkSession.builder \
    .appName("StreamingAnalytics") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Read incoming CSV files as a stream
sales_stream = spark.readStream \
    .option("header", True) \
    .option("inferSchema", True) \
    .schema("""
        timestamp TIMESTAMP,
        product STRING,
        city STRING,
        amount DOUBLE
    """) \
    .csv("input")

# Aggregate sales by product
result = sales_stream.groupBy(
    "product"
).agg(
    sum("amount").alias("total_revenue"),
    count("*").alias("number_of_orders")
)

# Write streaming results to console
query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="5 seconds") \
    .start()

query.awaitTermination()
