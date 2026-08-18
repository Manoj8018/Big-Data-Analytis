from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType, DoubleType

spark = SparkSession.builder \
    .appName("CustomUDF") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Sample customer data
data = [
    (1, "Manoj", 60000),
    (2, "Rahul", 45000),
    (3, "Arun", 75000),
    (4, "Kiran", 30000),
    (5, "Vijay", 90000)
]

df = spark.createDataFrame(
    data,
    ["id", "name", "salary"]
)

print("=== Original Data ===")
df.show()

# -----------------------------------
# UDF 1: Salary Category
# -----------------------------------

def salary_category(salary):
    if salary >= 70000:
        return "High"
    elif salary >= 40000:
        return "Medium"
    else:
        return "Low"

salary_udf = udf(
    salary_category,
    StringType()
)

result = df.withColumn(
    "salary_category",
    salary_udf(col("salary"))
)

print("=== Salary Category ===")
result.show()

# -----------------------------------
# UDF 2: Annual Salary
# -----------------------------------

def annual_salary(salary):
    return float(salary * 12)

annual_salary_udf = udf(
    annual_salary,
    DoubleType()
)

result = result.withColumn(
    "annual_salary",
    annual_salary_udf(col("salary"))
)

print("=== Final Result ===")
result.show()

spark.stop()
