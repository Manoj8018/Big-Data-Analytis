# BDA Exercise 8 & 9 – Apache Cassandra using Docker

## Objective

The objective of this exercise is to install Apache Cassandra using Docker on Ubuntu WSL, create a keyspace and tables, insert sample data, execute CQL queries, and understand Cassandra data modeling concepts.

---

## Software Requirements

- Ubuntu 26.04 LTS (WSL2)
- Java 21
- Docker 29.6.1
- Docker Compose v5.3.1
- Apache Cassandra
- CQLSH

---

## Project Structure

```
BDA_Exercise_8_9/
│── README.md
│── docker-compose.yml
│── setup_exercise.cql
│── generate_data.py
└── screenshots/
```

---

## Steps Performed

### 1. Installed Docker

Verified installation using:

```bash
docker --version
docker compose version
```

### 2. Started Cassandra

```bash
docker compose up -d
```

Verified using:

```bash
docker ps
```

### 3. Connected to Cassandra

```bash
docker exec -it cassandra cqlsh
```

### 4. Created Keyspace

Created the **sparkify** keyspace using the `SimpleStrategy` replication strategy.

### 5. Created Tables

Three tables were created:

- `song_info_by_session`
- `song_playing_history_by_user`
- `who_listened_to_song`

### 6. Inserted Sample Data

Inserted sample records into all three tables.

### 7. Executed Queries

#### Query 1

Retrieve all songs played in a session.

```sql
SELECT * FROM song_info_by_session
WHERE session_id = 100;
```

#### Query 2

Retrieve all songs played by a user during a session.

```sql
SELECT * FROM song_playing_history_by_user
WHERE user_id = 1
AND session_id = 100;
```

#### Query 3

Find all users who listened to a specific song.

```sql
SELECT * FROM who_listened_to_song
WHERE song = 'Hey Jude';
```

### 8. UPSERT

Verified that inserting a row with an existing primary key updates the existing record.

### 9. Consistency Level

Checked the current consistency level:

```sql
CONSISTENCY;
```

Output:

```
Current consistency level is ONE.
```

---

## Learning Outcomes

- Installed Apache Cassandra using Docker.
- Created a Cassandra keyspace.
- Designed tables based on query requirements.
- Inserted and queried data using CQL.
- Understood partition keys and clustering columns.
- Learned Cassandra UPSERT behavior.
- Explored consistency levels.

---

## Result

The Apache Cassandra database was successfully deployed using Docker on Ubuntu WSL. The Sparkify keyspace and all required tables were created, sample data was inserted successfully, and all required CQL queries produced the expected results.

---

## Author

**Manoj G**
