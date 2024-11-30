import sqlite3
import json


def import_from_json():
    db_path = 'art.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open('artists.json', 'r', encoding='utf-8') as file:
        artists_data = json.load(file)


    for artists in artists_data:
        cursor.execute("SELECT COUNT(*) FROM artists WHERE id = ?", (artists["id"],))
        count = cursor.fetchone()[0]

        if count == 0:  
            cursor.execute("INSERT INTO artists (id, name, birth_year, death_year) VALUES (?, ?, ?, ?)",
                           (artists["id"], artists["name"], artists["birth_year"], artists["death_year"]))

    conn.commit()

    conn.close()
    print("Импорт завершен! Данные импортированы из artists.json в базу данных.")
    input("Нажмите Enter для выхода...")

import_from_json()
