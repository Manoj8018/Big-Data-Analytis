# BDA Exercise 10 – Hadoop + Cassandra Integration

## Objective

Build a hybrid analytics system using Hadoop for batch processing and Apache Cassandra for real-time data storage.

## Technologies

- Ubuntu 26.04 LTS (WSL2)
- Hadoop 3.4.2
- Apache Cassandra (Docker)
- Python
- Hadoop Streaming
- HDFS

## Project Structure

```
hadoop-cassandra-exercise/
├── data/
├── jobs/
├── output/
├── scripts/
├── screenshots/
└── README.md
```

## Workflow

1. Generated batch data using Python.
2. Uploaded data to HDFS.
3. Processed data using Hadoop Streaming:
   - Daily Aggregates
   - Top Songs
4. Exported Hadoop output.
5. Loaded processed data into Cassandra.
6. Verified results using CQL queries.

## Learning Outcomes

- Hadoop Streaming MapReduce
- HDFS operations
- Cassandra data modeling
- Hadoop–Cassandra integration
- Batch analytics workflow

## Result

Successfully integrated Hadoop and Cassandra to process and store music streaming analytics.
