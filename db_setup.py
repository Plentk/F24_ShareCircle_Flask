import sqlite3
import json
from werkzeug.utils import secure_filename

sc_storage = "static/storage/"
sc_database = "sharecircle.db"
sc_json = "shareCircleItems.json"

conn = sqlite3.connect(f"{sc_storage}/{sc_database}")
cursor = conn.cursor()
cursor.execute("""
              DROP TABLE IF EXISTS category
              """)
cursor.execute("""
              DROP TABLE IF EXISTS items_to_donate
              """)
cursor.execute("""
              CREATE TABLE IF NOT EXISTS category (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL UNIQUE
              );""")
cursor.execute("""
              CREATE TABLE IF NOT EXISTS items_to_donate (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              description TEXT NOT NULL,
              location TEXT NOT NULL,
              create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              pickup_time TEXT NULL,
              image_filename TEXT,
              category_id INTEGER NOT NULL,
              FOREIGN KEY (category_id) REFERENCES category(id)
              );
              """)
conn.commit()
with open(f"{sc_storage}/{sc_json}", "r") as json_file:
  data = json.load(json_file)
print(data)
print(type(data))

for datum in data:
  print(datum)
  print(datum['category'])
  try:
    cursor.execute(f"""
                    SELECT id, name FROM category WHERE category.name == {datum['category']} 
                  """)
    detect = cursor.fetchall()
    for value in detect:
      print(detect)
  except:
    cursor.execute("""
                    INSERT INTO category(name) VALUES (?)
                   """, (datum['category']))