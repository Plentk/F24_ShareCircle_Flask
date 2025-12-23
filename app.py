from flask import Flask, render_template, request
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
  print("sc_main")
  return render_template("index.html")

@app.route("/home", methods=["GET", "POST"])
def sc_home():
  print("sc_home")
  return redirect(url_for("main"))

@app.route("/post", methods=["GET", "POST"])
def sc_post():
  if request.method == "POST":
    print("sc_post_true")
    # Queries form for all form data
    form_data = request.form
    title = form_data["title"]
    category = form_data["category"]
    description = form_data["description"]
    location = form_data["address"]
    # Query for image data
    image = request.files["file"]

    if image and image.filename != '':
      # Make filename safe
      filename = secure_filename(image.filename)

      # Save file
      image.save(os.path.join("static/uploads", filename))

      # Save information to database
      conn = connect_to_database(sc_database)
      cursor = conn.cursor()
      cursor.execute("""
                     INSERT INTO items_to_donate (title, description, location, image_filename, category_id) VALUES (?, ?, ?, ?, ?) 
                     """, (title, description, location, filename, category))
      
      conn.commit()
      conn.close()
      
      return redirect(url_for("home"))
    else:
      return render_template("post.html")


  else:
    print("sc_post")
    return render_template("post.html")

@app.route("/map")
def sc_map():
  print("sc_map")
  return render_template("map.html")

if __name__ == "__main__":
  print("everything all good?")
  app.run()