from flask import Flask
import sqlite3
import os
from werkzeug.utils import secure_filename

sc_database = ""
app = Flask(__name__)

def connect_to_database(database):
  conn = sqlite3.connect(database)
  
def init_database(database):
  conn = connect_to_database(database)
  cursor = conn.cursor()
  cursor.execute("""
                CREATE TABLE IF NOT EXISTS (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 category TEXT NOT NULL,
                 description TEXT NOT NULL,
                 location TEXT NOT NULL,
                 time TEXT NOT NULL,
                 filename TEXT
                 );
                 """)
  conn.commit()
  conn.close()

init_database(sc_database)

@app.route("/", methods=["GET", "POST"])
def sc_main():
  
  return render_template("home.html")

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