import sqlite3
from werkzeug.security import check_password_hash
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "dev-only-change-me"

@app.route("/login", methods=["GET", "POST"])
def login():
    error =""
    success = ""

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        connection = sqlite3.connect("fitness.db")
        connection.row_factory = sqlite3.Row

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(
            user["password"],
            password
        ):
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            success = "Logged in!"
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error, success=success)

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