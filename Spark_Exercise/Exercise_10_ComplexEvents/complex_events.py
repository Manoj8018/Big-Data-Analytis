from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    when,
    count,
    window
)

spark = SparkSession.builder \
    .appName("ComplexEventProcessing") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define schema for incoming events
schema = """
    timestamp TIMESTAMP,
    user_id INT,
    event_type STRING,
    amount DOUBLE
"""

# Read events as a streaming DataFrame
events = spark.readStream \
    .schema(schema) \
    .option("header", True) \
    .csv("input")

# Classify events
classified_events = events.withColumn(
    "event_status",
    when(col("amount") >= 50000, "SUSPICIOUS")
    .otherwise("NORMAL")
)

print("=== Event Classification ===")

# Aggregate events in 30-second windows
event_summary = classified_events.groupBy(
    window(col("timestamp"), "30 seconds"),
    "event_status"
).agg(
    count("*").alias("event_count")
)

# Write results to console
query = event_summary.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="5 seconds") \
    .start()

query.awaitTermination()
