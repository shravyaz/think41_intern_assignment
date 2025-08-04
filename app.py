from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# DB connect function
def connect_db():
    return sqlite3.connect("ecommerce.db")


# ✅ Route 1: Get all customers
@app.route("/customers", methods=["GET"])
def get_customers():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")  # table name is `user` (not users!)
        rows = cursor.fetchall()

        customers = []
        for row in rows:
            customers.append({
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "age": row[4],
                "gender": row[5],
                "state": row[6],
                "street_address": row[7],
                "postal_code": row[8],
                "city": row[9],
                "country": row[10],
                "latitude": row[11],
                "longitude": row[12],
                "traffic_source": row[13],
                "created_at": row[14]
            })

        return jsonify(customers), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Route 2: Get single customer with order count
@app.route("/customers/<int:user_id>", methods=["GET"])
def get_customer(user_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Get customer
        cursor.execute("SELECT * FROM user WHERE id=?", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Customer not found"}), 404

        # Get order count
        cursor.execute("SELECT COUNT(*) FROM orders WHERE user_id=?", (user_id,))
        order_count = cursor.fetchone()[0]

        customer_data = {
            "id": user[0],
            "first_name": user[1],
            "last_name": user[2],
            "email": user[3],
            "age": user[4],
            "gender": user[5],
            "state": user[6],
            "street_address": user[7],
            "postal_code": user[8],
            "city": user[9],
            "country": user[10],
            "latitude": user[11],
            "longitude": user[12],
            "traffic_source": user[13],
            "created_at": user[14],
            "order_count": order_count
        }

        return jsonify(customer_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)
