import sqlite3

conn = sqlite3.connect('art.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birth_year INTEGER,
        death_year INTEGER
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS paintings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        artist_id INTEGER,
        year INTEGER,
        FOREIGN KEY(artist_id) REFERENCES artists(id)
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS styles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        style_name TEXT
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS painting_styles (
        painting_id INTEGER,
        style_id INTEGER,
        FOREIGN KEY(painting_id) REFERENCES paintings(id),
        FOREIGN KEY(style_id) REFERENCES styles(id)
    )''')

conn.commit()
conn.close()
