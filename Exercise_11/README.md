# Exercise 11 – Apache Spark Word Count using PySpark

## Objective

The objective of this exercise is to install Apache Spark, configure the environment, and implement the Word Count program using PySpark DataFrames. The exercise demonstrates Spark's distributed data processing capabilities and basic DataFrame operations.

---

## Software Requirements

- Ubuntu (WSL/Linux)
- Java 21
- Apache Spark 4.2.0
- Python 3
- PySpark

---

## Folder Structure

```
Exercise_11/
│── word_count.py
│── sample.txt
│── README.md
```

---

## Installation

### Install Java

```bash
sudo apt update
sudo apt install openjdk-21-jdk -y
```

### Download Apache Spark

```bash
cd /tmp
wget https://dlcdn.apache.org/spark/spark-4.2.0/spark-4.2.0-bin-hadoop3.tgz
tar -xzf spark-4.2.0-bin-hadoop3.tgz
sudo mv spark-4.2.0-bin-hadoop3 /opt/spark
```

### Configure Environment Variables

```bash
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
```

Reload the configuration:

```bash
source ~/.bashrc
```

Verify installation:

```bash
spark-shell --version
```

---

## Running the Program

Start PySpark:

```bash
pyspark
```

Execute the code in **word_count.py** or run the commands in the PySpark shell.

---

## Input Data

The sample text file (`sample.txt`) contains:

```text
Apache Spark is fast
Spark is easy
Python works with Spark
Hello Spark
```

---

## Expected Output

```
+------+-----+
| word |count|
+------+-----+
|Spark | 4   |
|is    | 2   |
|Apache| 1   |
|fast  | 1   |
|easy  | 1   |
|Python| 1   |
|works | 1   |
|with  | 1   |
|Hello | 1   |
+------+-----+
```

---

## Concepts Covered

- Apache Spark Installation
- Java Configuration
- PySpark
- Spark DataFrames
- DataFrame Transformations
- Word Count Algorithm
- GroupBy Operation
- Sorting Results
- Reading Text Files

---

## Learning Outcome

After completing this exercise, the following concepts were understood:

- Installing and configuring Apache Spark
- Running PySpark applications
- Creating DataFrames
- Reading text files
- Splitting text into words
- Counting word frequency
- Sorting and displaying results
- Understanding Spark's distributed processing

---

## Author

**Name:** Manoj G

**Course:** Big Data Analytics

**Exercise:** 11 – Apache Spark Word Count using PySpark
