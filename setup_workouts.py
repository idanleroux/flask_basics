import sqlite3

connection = sqlite3.connect("fitness.db")
connection.execute("PRAGMA foreign_keys = ON")

connection.execute("""CREATE TABLE IF NOT EXISTS workouts (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
member_id TEXT NOT NULL,
workout_name TEXT NOT NULL,
duration INTEGER NOT NULL,
FOREIGN KEY (member_id) REFERENCES workouts (id))""")

connection.execute("DELETE FROM workouts")
connection.execute("DELETE FROM sqlite_sequence WHERE name = 'workouts'")

sample_workouts = [(1, "Full body", 45),
                   (1, "Cardio", 30),
                   (2, "Treadmill", 40),
                   (2, "Mobility", 25)]

connection.executemany("""INSERT INTO workouts (member_id, workout_name, duration)
VALUES (?, ?, ?)""", sample_workouts)

connection.commit()
connection.close()

print("New table created")