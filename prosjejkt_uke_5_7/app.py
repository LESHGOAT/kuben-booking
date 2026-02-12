from flask import Flask, jsonify, render_template, request, session, redirect
import mariadb
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "super-secret-key"
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per 10 minutes"])

load_dotenv(find_dotenv())

def get_db_connection():
    return mariadb.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )

# ---------------- FRONTEND ----------------
@app.route("/")
def frontend():
    if "user_id" not in session:
        return render_template("login.html")
    return render_template("index.html")

# ---------------- AUTH ----------------
@app.route("/login", methods=["POST"])
@limiter.limit("5 per 10 minutes")
def login():
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, brukertype, password FROM users WHERE email=?",
        (data["email"],)
    )
    user = cur.fetchone()
    conn.close()

    if user and check_password_hash(user[2], data["password"]):
        session["user_id"] = user[0]
        session["brukertype"] = user[1]
        return jsonify({"success": True})
    elif not user or not check_password_hash(user[2], data["password"]): return jsonify({"error": "Feil e-post eller passord"}), 401
    
    else:"prøv igjen om 10 minutter.for mange forsøk", 429


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or request.form

    navn = data.get("navn") or data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not navn or not email or not password:
        return jsonify({"error": "Alle felt må fylles ut"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    try:

        hashed_password = generate_password_hash(password)

        cur.execute(
         "INSERT INTO users (navn, brukertype, email, password) VALUES (?, ?, ?, ?)",
          (navn, "student", email, hashed_password)
    )
        conn.commit()
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 400

    conn.close()
    return jsonify({"success": True})


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------- ROOMS ----------------
@app.route("/rooms")
def get_rooms():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM rooms")
    rooms = cur.fetchall()
    conn.close()
    return jsonify(rooms)

# ---------------- AVAILABILITY ----------------
@app.route("/availability")
def availability():
    room_id = request.args.get("room_id")
    date = datetime.strptime(request.args.get("date"), "%Y-%m-%d")

    slots = []
    for h in range(7, 17):
        start = datetime.combine(date, datetime.min.time()) + timedelta(hours=h)
        end = start + timedelta(hours=1)
        slots.append({
            "start": start.strftime("%H:%M"),
            "end": end.strftime("%H:%M"),
            "available": True
        })

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT start_time, end_time FROM bookings WHERE room_id=? AND DATE(start_time)=?",
        (room_id, date.date())
    )
    bookings = cur.fetchall()
    conn.close()

    for b in bookings:
        b_start = b[0].strftime("%H:%M")
        b_end = b[1].strftime("%H:%M")
        for s in slots:
            if not (s["end"] <= b_start or s["start"] >= b_end):
                s["available"] = False

    return jsonify(slots)

# ---------------- BOOKING ----------------
@app.route("/bookings", methods=["POST"])
def book():
    if "user_id" not in session:
        return jsonify({"error": "Ikke innlogget"}), 403

    # 👇 NY SJEKK
    if session.get("brukertype") == "student":
        return jsonify({"error": "Studenter kan ikke booke rom"}), 403

    data = request.json
    start = datetime.strptime(f"{data['date']} {data['start_time']}", "%Y-%m-%d %H:%M")
    end = datetime.strptime(f"{data['date']} {data['end_time']}", "%Y-%m-%d %H:%M")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO bookings (user_id, room_id, start_time, end_time) VALUES (?, ?, ?, ?)",
        (session["user_id"], data["room_id"], start, end)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True})


# ---------------- MINE BOOKINGER ----------------
@app.route("/my-bookings")
def my_bookings():
    if "user_id" not in session:
        return jsonify([])

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT b.id, r.navn, b.start_time, b.end_time
        FROM bookings b
        JOIN rooms r ON b.room_id = r.id
        WHERE b.user_id=?
        ORDER BY b.start_time
    """, (session["user_id"],))
    rows = cur.fetchall()
    conn.close()

    bookings = []
    for r in rows:
        bookings.append({
            "id": r[0],
            "room": r[1],
            "start": r[2].strftime("%Y-%m-%d %H:%M"),
            "end": r[3].strftime("%H:%M")
        })

    return jsonify(bookings)

# ---------------- SLETT BOOKING ----------------
@app.route("/bookings/<int:booking_id>", methods=["DELETE"])
def delete_booking(booking_id):
    if "user_id" not in session:
        return jsonify({"error": "Ikke innlogget"}), 403

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM bookings WHERE id=? AND user_id=?",
        (booking_id, session["user_id"])
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
