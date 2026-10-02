import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('fitness.db')

connection.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL UNIQUE,
password_hash TEXT NOT NULL
)
""")

connection.execute("DELETE FROM users")

demo_hash = generate_password_hash("ClassDemo!2026")

connection.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                   ("student", demo_hash))

connection.commit()
connection.close()

print("User created successfully!")