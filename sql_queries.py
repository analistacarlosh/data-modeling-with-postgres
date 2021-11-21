# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

user_table_create = ("CREATE TABLE IF NOT EXISTS users"\
" (user_id INT NOT NULL PRIMARY KEY, first_name VARCHAR NOT NULL,"\
" last_name VARCHAR, gender VARCHAR NOT NULL, level VARCHAR NOT NULL)")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists"\
                      " (artists_id VARCHAR NOT NULL PRIMARY KEY,"\
                      " name VARCHAR NOT NULL, location VARCHAR, latitude FLOAT, longitude FLOAT)")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs"\
" (song_id VARCHAR NOT NULL PRIMARY KEY, title VARCHAR NOT NULL,"\
" artist_id VARCHAR REFERENCES artists ON DELETE CASCADE,"\
" year INT NOT NULL, duration FLOAT NOT NULL)")

time_table_create = ("CREATE TABLE IF NOT EXISTS time"\
" (time_id SERIAL PRIMARY KEY, start_time TIME, hour INT,"\
" day VARCHAR, week INT, month INT, year INT, "\
" weekday INT)")

songplay_table_create = ("CREATE TABLE songplays"\
" (songplay_id SERIAL PRIMARY KEY, start_time TIME,"\
" user_id INT REFERENCES users ON DELETE CASCADE,"\
" level VARCHAR,"\
" song_id VARCHAR REFERENCES songs ON DELETE CASCADE,"\
" artist_id VARCHAR REFERENCES artists ON DELETE CASCADE,"\
" session_id VARCHAR, location VARCHAR, user_agent VARCHAR)")

# INSERT RECORDS

user_table_insert = ("INSERT INTO users"\
" (user_id, first_name, last_name, gender, level)"\
" VALUES (%s, %s, %s, %s, %s)")

artist_table_insert = ("INSERT INTO artists"\
" (artists_id, name, location, latitude, longitude)"\
" VALUES (%s, %s, %s, %s, %s)")

song_table_insert = ("INSERT INTO songs"\
" (song_id, title, artist_id, year, duration)"\
" VALUES (%s, %s, %s, %s, %s)")

time_table_insert = ("INSERT INTO time"\
" (start_time, hour, day, week, month, year, weekday)"\
" VALUES (%s, %s, %s, %s, %s, %s, %s)")

songplay_table_insert = ("INSERT INTO songplays"\
" (start_time, user_id, level, song_id, artist_id, session_id)"\
" VALUES (%s, %s, %s, %s, %s, %s)")

# FIND SONGS
song_select = ("""
SELECT s.song_id, s.artist_id, a.name FROM songs as s LEFT JOIN artists as a ON s.artist_id = a.artists_id WHERE s.title = %s AND a.name = %s AND s.duration = %s """)

# QUERY LISTS
create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, time_table_drop, song_table_drop, artist_table_drop, user_table_drop]