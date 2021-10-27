# DROP TABLES

songplay_table_drop = "DROP TABLE songplay"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

user_table_create = ("CREATE TABLE IF NOT EXISTS users"\
"(user_id INT NOT NULL PRIMARY KEY, first_name VARCHAR NOT NULL,"\
"last_name VARCHAR, gender VARCHAR NOT NULL, level VARCHAR NOT NULL)")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists"\
                      "(artists_id VARCHAR NOT NULL PRIMARY KEY,"\
                      "name VARCHAR NOT NULL, location VARCHAR, latitude FLOAT, longitude FLOAT)")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs"\
"(song_id VARCHAR NOT NULL PRIMARY KEY, title VARCHAR NOT NULL,"\
"artist_id VARCHAR REFERENCES artists ON DELETE CASCADE,"\
"year INT NOT NULL, duration FLOAT NOT NULL)")

time_table_create = ("CREATE TABLE IF NOT EXISTS time"\ 
"(start_time TIME, hour INT, day VARCHAR,"\
"week INT, month INT, year INT,"\
"weekday INT)"\
)

songplay_table_create = ("CREATE TABLE songplays"/
"(songplay_id INT PRIMARY KEY, start_time TIME,"\
"user_id INT REFERENCES users ON DELETE CASCADE,"\
"level VARCHAR,"\
"song_id VARCHAR REFERENCES songs ON DELETE CASCADE,"\
"artist_id VARCHAR REFERENCES artists ON DELETE CASCADE,"\
"session_id VARCHAR, location VARCHAR, user_agent VARCHAR)")

# INSERT RECORDS

user_table_insert = ("INSERT INTO users"\
"(user_id, first_name, last_name, gender, level)"\
"VALUES (1, 'Carlos', 'Rodrigues', 'f', 'free')")

artist_table_insert = ("INSERT INTO artists"\
"(artists_id, name, location, latitude, longitude)"\
"VALUES ('fafasfasfaf', 'Charles', 'Braganca Paulista, SP, Brazil', 22.9532, 46.5423)")

song_table_insert = ("INSERT INTO songs"\
"(song_id, title, artist_id, year, duration)"\
"VALUES ('SOUPIRU12A6D4FA1E1', 'Der Kleine Dompfaff', 'ARJIE2Y1187B994AB7', 0, 152.92036)")

time_table_insert = ("INSERT INTO time"\
"(start_time, hour, day, week, month, year, weekday)"\
"VALUES (10:00, 1, 2, 1, 1, 2021, 1)")

songplay_table_insert = ("INSERT INTO songplays"\
"(songplay_id, start_time, user_id, level, song_id, artist_id, session_id)"\
"VALUES (1, 10:00, 1, 'free', 'SOUPIRU12A6D4FA1E1', 'fafasfasfaf', 100)")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]