#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import sqlite3
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=UTF-8")
print()

html_template = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>База данных: Искусство</title>
</head>
<body>
    <h2>Таблица художников</h2>
    <table border="1">
        <tr>
            <th>Имя</th>
            <th>Год рождения</th>
            <th>Год смерти</th>
        </tr>
        {artists_rows}
    </table>

    <h2>Таблица картин</h2>
    <table border="1">
        <tr>
            <th>Название картины</th>
            <th>ID художника</th>
            <th>Год создания</th>
        </tr>
        {paintings_rows}
    </table>

    <h2>Таблица стилей</h2>
    <table border="1">
        <tr>
            <th>Название стиля</th>
        </tr>
        {styles_rows}
    </table>

    <h2>Таблица стилей картин</h2>
    <table border="1">
        <tr>
            <th>ID картины</th>
            <th>ID стиля</th>
        </tr>
        {painting_styles_rows}
    </table>

    <h1>Добавить нового художника</h1>
    <form method="post" action="/cgi-bin/cgi_server.py">
        <label for="artist_name">Имя художника:</label>
        <input type="text" id="artist_name" name="artist_name" required><br><br>
        
        <label for="birth_year">Год рождения:</label>
        <input type="number" id="birth_year" name="birth_year" required><br><br>
        
        <label for="death_year">Год смерти:</label>
        <input type="number" id="death_year" name="death_year"><br><br>
        
        <input type="submit" value="Добавить художника">
    </form>

    <h1>Добавить картину</h1>
    <form method="post" action="/cgi-bin/cgi_server.py">
        <label for="painting_title">Название картины:</label>
        <input type="text" id="painting_title" name="painting_title" required><br><br>
        
        <label for="artist_id">ID художника:</label>
        <input type="number" id="artist_id" name="artist_id" required><br><br>
        
        <label for="painting_year">Год создания картины:</label>
        <input type="number" id="painting_year" name="painting_year" required><br><br>
        
        <input type="submit" value="Добавить картину">
    </form>

    <h1>Добавить стиль</h1>
    <form method="post" action="/cgi-bin/cgi_server.py">
        <label for="style_name">Название стиля:</label>
        <input type="text" id="style_name" name="style_name" required><br><br>
        
        <input type="submit" value="Добавить стиль">
    </form>

    <h2>Художники и их картины</h2>
    <table border="1">
        <tr>
            <th>Имя художника</th>
            <th>Название картины</th>
        </tr>
        {artists_paintings_rows}
    </table>

    <h2>Картины и их стили</h2>
    <table border="1">
        <tr>
            <th>Название картины</th>
            <th>Стиль</th>
        </tr>
        {paintings_styles_rows}
    </table>

    <h2>Художники в стиле "Cubism"</h2>
    <table border="1">
        <tr>
            <th>Имя художника</th>
        </tr>
        {cubism_artists_rows}
    </table>

</body>
</html>
"""


db_path_art = 'art.db'
conn_art = sqlite3.connect(db_path_art)
cursor_art = conn_art.cursor()


cursor_art.execute('''
SELECT a.name, p.title
FROM artists a
LEFT JOIN paintings p ON a.id = p.artist_id
''')
artists_paintings_rows = cursor_art.fetchall()


cursor_art.execute('''
SELECT p.title, s.style_name
FROM paintings p
LEFT JOIN painting_styles ps ON p.id = ps.painting_id
LEFT JOIN styles s ON ps.style_id = s.id
''')
paintings_styles_rows = cursor_art.fetchall()


cursor_art.execute('''
SELECT a.name
FROM artists a
JOIN paintings p ON a.id = p.artist_id
JOIN painting_styles ps ON p.id = ps.painting_id
JOIN styles s ON ps.style_id = s.id
WHERE s.style_name = 'Cubism'
''')
cubism_artists_rows = cursor_art.fetchall()


cursor_art.execute('SELECT * FROM artists')
artists_rows = cursor_art.fetchall()


cursor_art.execute('SELECT * FROM paintings')
paintings_rows = cursor_art.fetchall()


cursor_art.execute('SELECT * FROM styles')
styles_rows = cursor_art.fetchall()


cursor_art.execute('SELECT * FROM painting_styles')
painting_styles_rows = cursor_art.fetchall()


form = cgi.FieldStorage()


artist_name = form.getvalue("artist_name")
birth_year = form.getvalue("birth_year")
death_year = form.getvalue("death_year")

if artist_name and birth_year:
    cursor_art.execute("INSERT INTO artists (name, birth_year, death_year) VALUES (?, ?, ?)",
                       (artist_name, int(birth_year), int(death_year) if death_year else None))
    conn_art.commit()

painting_title = form.getvalue("painting_title")
artist_id = form.getvalue("artist_id")
painting_year = form.getvalue("painting_year")

if painting_title and artist_id and painting_year:
    cursor_art.execute("INSERT INTO paintings (title, artist_id, year) VALUES (?, ?, ?)",
                       (painting_title, int(artist_id), int(painting_year)))
    conn_art.commit()

style_name = form.getvalue("style_name")

if style_name:
    cursor_art.execute("INSERT INTO styles (style_name) VALUES (?)", (style_name,))
    conn_art.commit()

artists_paintings_html = ""
for row in artists_paintings_rows:
    artists_paintings_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
    </tr>
    """

paintings_styles_html = ""
for row in paintings_styles_rows:
    paintings_styles_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
    </tr>
    """

cubism_artists_html = ""
for row in cubism_artists_rows:
    cubism_artists_html += f"""
    <tr>
        <td>{row[0]}</td>
    </tr>
    """

artists_html = ""
for row in artists_rows:
    artists_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

paintings_html = ""
for row in paintings_rows:
    paintings_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

styles_html = ""
for row in styles_rows:
    styles_html += f"""
    <tr>
        <td>{row[1]}</td>
    </tr>
    """

painting_styles_html = ""
for row in painting_styles_rows:
    painting_styles_html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
    </tr>
    """

conn_art.close()

print(html_template.format(
    artists_paintings_rows=artists_paintings_html,
    paintings_styles_rows=paintings_styles_html,
    cubism_artists_rows=cubism_artists_html,
    artists_rows=artists_html,
    paintings_rows=paintings_html,
    styles_rows=styles_html,
    painting_styles_rows=painting_styles_html
)) 
#python -m http.server --cgi 8000