import sqlite3

connection = sqlite3.connect("fitness.db")

connection.execute("DROP TABLE IF EXISTS members")

connection.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        goal TEXT NOT NULL
    )
""")

sample_members = [
    ("alex", "Build strength"),
    ("Sam", "Improve fitness"),
    ("Jamie", "Run 5K"),
    ("Tayloe", "Improve flexibility")
]

connection.executemany("""
    INSERT INTO members (name, goal)
    VALUES (?, ?)
""", sample_members)

connection.commit()
connection.close()

print("Database created")