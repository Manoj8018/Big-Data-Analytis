from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("SparkMLPipeline") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Sample customer data
data = [
    (1, 25, 30000, 2, 0),
    (2, 30, 45000, 5, 1),
    (3, 22, 25000, 1, 0),
    (4, 35, 60000, 8, 1),
    (5, 28, 40000, 4, 1),
    (6, 40, 70000, 9, 1),
    (7, 21, 22000, 1, 0),
    (8, 26, 35000, 3, 0),
    (9, 32, 50000, 7, 1),
    (10, 24, 28000, 2, 0),
    (11, 38, 65000, 8, 1),
    (12, 29, 42000, 5, 1),
    (13, 20, 20000, 1, 0),
    (14, 34, 55000, 6, 1),
    (15, 27, 37000, 3, 0),
    (16, 42, 80000, 10, 1),
    (17, 23, 24000, 1, 0),
    (18, 31, 48000, 6, 1),
    (19, 26, 33000, 2, 0),
    (20, 36, 62000, 8, 1)
]

columns = [
    "customer_id",
    "age",
    "income",
    "purchases",
    "label"
]

df = spark.createDataFrame(data, columns)

print("=== Input Data ===")
df.show()

# Feature engineering
assembler = VectorAssembler(
    inputCols=["age", "income", "purchases"],
    outputCol="features"
)

# Random Forest classifier
rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    numTrees=20,
    seed=42
)

# Create ML pipeline
pipeline = Pipeline(
    stages=[assembler, rf]
)

# Train/test split
train_data, test_data = df.randomSplit(
    [0.8, 0.2],
    seed=42
)

print("Training records:", train_data.count())
print("Testing records:", test_data.count())

# Train model
model = pipeline.fit(train_data)

# Predictions
predictions = model.transform(test_data)

print("=== Predictions ===")

predictions.select(
    "customer_id",
    "age",
    "income",
    "purchases",
    "label",
    "prediction",
    "probability"
).show(truncate=False)

# Evaluate model
evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)

print("=== Model Evaluation ===")
print(f"Accuracy: {accuracy:.4f}")

spark.stop()
