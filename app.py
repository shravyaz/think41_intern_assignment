from flask import Flask, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

def connect_db():
    return sqlite3.connect("ecommerce.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customers")
def get_customers():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    customers = []
    for row in rows:
        cursor.execute("SELECT COUNT(*) FROM orders WHERE user_id = ?", (row[0],))
        order_count = cursor.fetchone()[0]
        customers.append({
            "id": row[0],
            "name": f"{row[1]} {row[2]}",
            "email": row[3],
            "order_count": order_count
        })
    return jsonify(customers)
