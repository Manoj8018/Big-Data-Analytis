import random
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('sparkify')

# Sample data
artists = [
    'The Beatles', 'Led Zeppelin', 'Pink Floyd', 'Queen', 'Nirvana',
    'Michael Jackson', 'Madonna', 'U2', 'Eagles', 'AC/DC'
]

songs = [
    'Hey Jude', 'Stairway to Heaven', 'Comfortably Numb',
    'Bohemian Rhapsody', 'Smells Like Teen Spirit',
    'Billie Jean', 'Like a Prayer', 'With or Without You',
    'Hotel California', 'Back in Black'
]

first_names = [
    'John', 'Jane', 'Robert', 'Mary',
    'James', 'Patricia', 'Michael', 'Jennifer'
]

last_names = [
    'Doe', 'Smith', 'Johnson', 'Williams',
    'Brown', 'Jones', 'Garcia', 'Miller'
]

# Generate 100 records
for i in range(100):
    session_id = random.randint(100, 999)
    user_id = random.randint(1, 50)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Insert into song_info_by_session
    for j in range(1, random.randint(2, 10)):
        session.execute("""
        INSERT INTO song_info_by_session
        (session_id, item_in_session, artist, song, length)
        VALUES (%s, %s, %s, %s, %s)
        """, (
            session_id,
            j,
            random.choice(artists),
            random.choice(songs),
            round(random.uniform(2.5, 10.0), 2)
        ))

    # Insert into song_playing_history_by_user
    for j in range(1, random.randint(2, 5)):
        session.execute("""
        INSERT INTO song_playing_history_by_user
        (user_id, session_id, item_in_session, artist, song, first_name, last_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            user_id,
            session_id,
            j,
            random.choice(artists),
            random.choice(songs),
            first_name,
            last_name
        ))

print("Data generation complete!")

cluster.shutdown()
