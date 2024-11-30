import sqlite3
from xml.dom.minidom import Document


def export_to_xml():
    db_path = 'art.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM artists")
    artists_rows = cursor.fetchall()

    doc = Document()

    root = doc.createElement('artists')
    doc.appendChild(root)

    for row in artists_rows:
        planet = doc.createElement('artists')
        root.appendChild(planet)

        id_element = doc.createElement('id')
        id_element.appendChild(doc.createTextNode(str(row[0])))
        planet.appendChild(id_element)

        name_element = doc.createElement('name')
        name_element.appendChild(doc.createTextNode(row[1]))
        planet.appendChild(name_element)

        dob_element = doc.createElement('birth_year')
        dob_element.appendChild(doc.createTextNode(str(row[2])))
        planet.appendChild(dob_element)

        dod_element = doc.createElement('death_year')
        dod_element.appendChild(doc.createTextNode(str(row[3])))
        planet.appendChild(dod_element)

    with open('artists.xml', 'w', encoding='utf-8') as file:
        file.write(doc.toprettyxml(indent="  "))

    conn.close()
    print("Экспорт завершен! Данные сохранены в artists.xml.")
    input("Нажмите Enter для выхода...")


export_to_xml()
