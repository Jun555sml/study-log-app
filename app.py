from cs50 import SQL
from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key"

db = SQL("sqlite:///project.db")


# Home
@app.route("/")
def index():

    # if not logged in
    if "user_id" not in session:
        return redirect("/login")

    # total study time
    total = db.execute(
        "SELECT SUM(minutes) AS total FROM studies WHERE user_id = ?",
        session["user_id"]
    )[0]["total"]

    # recent study logs
    recent = db.execute(
        """
        SELECT category, content, minutes, created_at
        FROM studies
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT 5
        """,
        session["user_id"]
    )
    return render_template("index.html", total=total or 0, recent=recent)


# register user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            flash("missing username or password or confirmation", "danger")
            return redirect("/register")

        if password != confirmation:
            flash("passwords do not match", "danger")
            return redirect("/register")

        hash_pw = generate_password_hash(password)

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username, hash_pw
            )
        except:
            return "username already exists"

        return redirect("/login")

    return render_template("register.html")


# login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method =="POST":
        session.clear()

        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username or password", "danger")
            return redirect("/login")

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    return render_template("login.html")


# logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# add learning content
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        category = request.form.get("category")
        content = request.form.get("content")
        note = request.form.get("note")
        minutes = request.form.get("minutes")

        if not category or not content:
            flash("Category and Content are required.", "danger")
            return redirect("/add")

        db.execute(
            """
            INSERT INTO studies (user_id, category, content, note, minutes)
            VALUES (?, ?, ?, ?, ?)
            """,
            session["user_id"],
            category,
            content,
            note,
            minutes
        )

        return redirect("/")

    return render_template("add.html")


#see history
@app.route("/history")
def history():
    rows = db.execute(
        """
        SELECT id, category, content, note, minutes, created_at
        FROM studies
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        session["user_id"]
    )
    return render_template("history.html", rows=rows)


#delete
@app.route("/delete", methods=["POST"])
def delete():
    study_id = request.form.get("id")
    if not study_id:
        return redirect("/history")

    db.execute(
        "DELETE FROM studies WHERE id = ? AND user_id = ?",
        study_id, session["user_id"]
    )
    return redirect("/history")


# edit history
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        study_id = request.args.get("id")
        row = db.execute(
            "SELECT * FROM studies WHERE id = ? AND user_id = ?",
            study_id, session["user_id"]
        )
        if len(row) != 1:
            return redirect("/history")

        return render_template("edit.html", row=row[0])

    # update
    study_id = request.form.get("id")
    category = request.form.get("category")
    content = request.form.get("content")
    note = request.form.get("note")
    minutes = request.form.get("minutes")

    db.execute(
        """
        UPDATE studies
        SET category = ?, content = ?, note = ?, minutes = ?
        WHERE id = ? AND user_id = ?
        """,
        category, content, note, minutes, study_id, session["user_id"]
    )
    return redirect("/history")


if __name__ == "__main__":
    app.run(debug=True)
