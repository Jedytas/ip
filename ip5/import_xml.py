import sqlite3
from xml.dom import minidom

def import_from_xml():
    db_path = 'art.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    doc = minidom.parse('artists.xml')
    artists = doc.getElementsByTagName('artists')

    for artist in artists:
        artists_id = int(artist.getElementsByTagName('id')[0].childNodes[0].data)
        name = artist.getElementsByTagName('name')[0].childNodes[0].data
        dob = int(artist.getElementsByTagName('birth_year')[0].childNodes[0].data)
        dod = int(artist.getElementsByTagName('death_year')[0].childNodes[0].data)

        # Проверка на существование записи
        cursor.execute("SELECT COUNT(*) FROM artists WHERE id = ?", (artists_id,))
        count = cursor.fetchone()[0]

        if count == 0:  # Если записи нет, вставляем новую
            cursor.execute("INSERT INTO artists (id, name, birth_year, death_year) VALUES (?, ?, ?, ?)",
                           (artists_id, name, dob, dod))


    conn.commit()
    conn.close()
    print("Импорт из XML завершён!")
    input("Нажмите Enter для выхода...")

import_from_xml()
