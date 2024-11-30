import sqlite3

conn = sqlite3.connect('art.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO artists (name, birth_year, death_year) VALUES ('Vincent van Gogh', 1853, 1890)")
cursor.execute("INSERT INTO artists (name, birth_year, death_year) VALUES ('Pablo Picasso', 1881, 1973)")
cursor.execute("INSERT INTO artists (name, birth_year, death_year) VALUES ('Leonardo da Vinci', 1452, 1519)")

cursor.execute("INSERT INTO paintings (title, artist_id, year) VALUES ('Starry Night', 1, 1889)")
cursor.execute("INSERT INTO paintings (title, artist_id, year) VALUES ('Guernica', 2, 1937)")
cursor.execute("INSERT INTO paintings (title, artist_id, year) VALUES ('Mona Lisa', 3, 1503)")

cursor.execute("INSERT INTO styles (style_name) VALUES ('Post-Impressionism')")
cursor.execute("INSERT INTO styles (style_name) VALUES ('Cubism')")
cursor.execute("INSERT INTO styles (style_name) VALUES ('Renaissance')")

cursor.execute("INSERT INTO painting_styles (painting_id, style_id) VALUES (1, 1)")
cursor.execute("INSERT INTO painting_styles (painting_id, style_id) VALUES (2, 2)")
cursor.execute("INSERT INTO painting_styles (painting_id, style_id) VALUES (3, 3)")


conn.commit()
conn.close()
