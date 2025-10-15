from flask import Flask, request, jsonify, abort
import os, psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db-endpoint-placeholder.rds.amazonaws.com")
DB_NAME = os.getenv("DB_NAME", "notesdb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "fakepassword")
API_KEY = os.getenv("API_KEY", "fakeapikey")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, connect_timeout=5
    )

@app.before_request
def require_api_key():
    if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
        key = request.headers.get("X-API-KEY")
        if key != API_KEY:
            abort(401)

@app.route("/")
def home():
    return "AWS Flask App is running!"

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json(silent=True) or {}
    content = data.get("content")
    if not content:
        return jsonify({"error": "Content required"}), 400
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (%s) RETURNING id;", (content,))
    note_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": note_id, "content": content}), 201

@app.route("/notes", methods=["GET"])
def get_notes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, content FROM notes ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "content": r[1]} for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
