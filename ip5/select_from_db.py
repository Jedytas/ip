import sqlite3

conn = sqlite3.connect('art.db')
cursor = conn.cursor()


cursor.execute('''
SELECT a.name AS artist_name, a.birth_year, a.death_year, p.title AS painting_title
FROM artists a
LEFT JOIN paintings p ON a.id = p.artist_id
''')
print(cursor.fetchall())


cursor.execute('''
SELECT p.title AS painting_title, s.style_name
FROM paintings p
LEFT JOIN painting_styles ps ON p.id = ps.painting_id
LEFT JOIN styles s ON ps.style_id = s.id
''')
print(cursor.fetchall())


cursor.execute('''
SELECT a.name AS artist_name, a.birth_year, a.death_year
FROM artists a
JOIN paintings p ON a.id = p.artist_id
JOIN painting_styles ps ON p.id = ps.painting_id
JOIN styles s ON ps.style_id = s.id
WHERE s.style_name = 'Cubism'
''')
print(cursor.fetchall())

conn.close()
