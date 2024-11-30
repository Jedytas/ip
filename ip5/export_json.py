import sqlite3
import json

def export_to_json():
    db_path = 'art.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM artists")
    artists_rows = cursor.fetchall()

    artists_data = []
    for row in artists_rows:
        planet = {
            "id": row[0],
            "name": row[1],
            "birth_year": row[2],
            "death_year": row[3]
        }
        artists_data.append(planet)

    with open('artists.json', 'w', encoding='utf-8') as file:
        json.dump(artists_data, file, ensure_ascii=False, indent=4)

    conn.close()
    print("Экспорт завершен! Данные сохранены в artists.json.")
    input("Нажмите Enter для выхода...")

export_to_json()
