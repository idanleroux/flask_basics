import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def members():
    connection = sqlite3.connect("fitness.db")
    connection.row_factory = sqlite3.Row

    member_rows = connection.execute(
        "SELECT * FROM members ORDER BY name").fetchall()

    connection.close()
    return render_template("L7.html", members=member_rows)

if __name__ == "__main__":
    app.run(debug=True)