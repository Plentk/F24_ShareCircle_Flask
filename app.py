from flask import Flask
import sqlite3
import os
from werkzeug.utils import secure_filename

sc_database = "sharecircle.db"
app = Flask(__name__)

def connect_to_database(database):
  conn = sqlite3.connect(database)
  return conn
  
def init_database(database):
  conn = connect_to_database(database)
  cursor = conn.cursor()
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
  conn.close()

init_database(sc_database)

@app.route("/", methods=["GET", "POST"])
def sc_main():
  conn = connect_to_database(sc_database)
  cursor = conn.cursor()
  cursor.execute("""
                 """)
  return render_template("index.html")

@app.route("/home", methods=["GET", "POST"])
def sc_home():
  return redirect(url_for("main"))

@app.route("/post", methods=["GET", "POST"])
def sc_post():
  return render_template("post.html")

@app.route("/map")
def sc_map():
  return render_template("map.html")

if __name__ == "__main__":
  app.run()