from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("WordCountRDD") \
    .getOrCreate()

sc = spark.sparkContext

# Read input file
text_file = sc.textFile("sample.txt")

# Word Count using RDD transformations
word_counts = (
    text_file
    .flatMap(lambda line: line.split())
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

# Display results
for word, count in word_counts.collect():
    print(f"{word}: {count}")

spark.stop()
