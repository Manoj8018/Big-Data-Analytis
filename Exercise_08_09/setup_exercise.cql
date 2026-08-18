-- ============================================
-- CASSANDRA EXERCISE: SPARKIFY MUSIC STREAMING
-- ============================================

CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
    'class': 'SimpleStrategy',
    'replication_factor': '1'
};

USE sparkify;

CREATE TABLE IF NOT EXISTS song_info_by_session (
    artist TEXT,
    song TEXT,
    length DECIMAL,
    session_id INT,
    item_in_session INT,
    PRIMARY KEY (session_id, item_in_session)
) WITH CLUSTERING ORDER BY (item_in_session ASC);

CREATE TABLE IF NOT EXISTS song_playing_history_by_user (
    artist TEXT,
    song TEXT,
    first_name TEXT,
    last_name TEXT,
    session_id INT,
    item_in_session INT,
    user_id INT,
    PRIMARY KEY ((user_id, session_id), item_in_session)
) WITH CLUSTERING ORDER BY (item_in_session DESC);

CREATE TABLE IF NOT EXISTS who_listened_to_song (
    user_id INT,
    first_name TEXT,
    last_name TEXT,
    song TEXT,
    PRIMARY KEY (song, user_id)
);

-- Sample Data

INSERT INTO song_info_by_session (session_id, item_in_session, artist, song, length)
VALUES (100, 1, 'The Beatles', 'Hey Jude', 7.11);

INSERT INTO song_info_by_session (session_id, item_in_session, artist, song, length)
VALUES (100, 2, 'Led Zeppelin', 'Stairway to Heaven', 8.02);

INSERT INTO song_info_by_session (session_id, item_in_session, artist, song, length)
VALUES (100, 3, 'Pink Floyd', 'Comfortably Numb', 6.53);

INSERT INTO song_info_by_session (session_id, item_in_session, artist, song, length)
VALUES (101, 1, 'Queen', 'Bohemian Rhapsody', 5.55);

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (1, 100, 1, 'The Beatles', 'Hey Jude', 'John', 'Doe');

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (1, 100, 2, 'Led Zeppelin', 'Stairway to Heaven', 'John', 'Doe');

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (1, 100, 3, 'Pink Floyd', 'Comfortably Numb', 'John', 'Doe');

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (2, 200, 1, 'Queen', 'Bohemian Rhapsody', 'Jane', 'Smith');

INSERT INTO who_listened_to_song (song, user_id, first_name, last_name)
VALUES ('Hey Jude', 1, 'John', 'Doe');

INSERT INTO who_listened_to_song (song, user_id, first_name, last_name)
VALUES ('Hey Jude', 2, 'Jane', 'Smith');

INSERT INTO who_listened_to_song (song, user_id, first_name, last_name)
VALUES ('Comfortably Numb', 1, 'John', 'Doe');

-- Sample Queries

SELECT * FROM song_info_by_session WHERE session_id = 100;

SELECT * FROM song_playing_history_by_user
WHERE user_id = 1 AND session_id = 100;

SELECT * FROM who_listened_to_song
WHERE song = 'Hey Jude';
