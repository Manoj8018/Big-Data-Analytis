from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, desc

spark = SparkSession.builder.appName("WordCount").getOrCreate()

df = spark.createDataFrame([
    ("Hello world Hello Spark",),
    ("Spark is great for big data",),
    ("Hello Python and Spark",)
], ["line"])

words_df = df.select(explode(split(col("line"), " ")).alias("word"))

word_counts = words_df.groupBy("word").count()

word_counts.orderBy(desc("count")).show()

spark.stop()
