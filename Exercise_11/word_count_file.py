from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, desc

spark = SparkSession.builder.appName("WordCountFile").getOrCreate()

# Read text file
df = spark.read.text("sample.txt")

# Split lines into words
words_df = df.select(
    explode(split(col("value"), " ")).alias("word")
)

# Count words
word_counts = words_df.groupBy("word").count()

# Display results
word_counts.orderBy(desc("count")).show()

spark.stop()
