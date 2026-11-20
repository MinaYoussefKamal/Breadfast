from flask import Flask, render_template, request, jsonify
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "cafeteria.db"

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

SEED_MENU = [
    ("Cheese Sandwich", "Fresh cheese sandwich", 35.00, "🥪", 1),
    ("Chicken Sandwich", "Grilled chicken with fresh vegetables", 55.00, "🥙", 1),
    ("French Fries", "Crispy golden fries", 30.00, "🍟", 1),
    ("Fresh Juice", "Seasonal fresh juice", 25.00, "🧃", 1),
    ("Bottled Water", "Cold bottled water", 10.00, "💧", 1),
    ("Chocolate Muffin", "Soft chocolate muffin", 28.00, "🧁", 0),
]


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS menu_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                emoji TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                pickup_time TEXT NOT NULL,
                pickup_place TEXT NOT NULL,
                total REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'Placed',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
                menu_item_id INTEGER NOT NULL REFERENCES menu_items(id),
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                unit_price REAL NOT NULL
            );
        """)
        count = db.execute("SELECT COUNT(*) FROM menu_items").fetchone()[0]
        if count == 0:
            db.executemany(
                """INSERT INTO menu_items
                   (name, description, price, emoji, available)
                   VALUES (?, ?, ?, ?, ?)""",
                SEED_MENU
            )


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/kitchen")
def kitchen_page():
    return render_template("kitchen.html")


@app.get("/api/menu")
def menu():
    with get_db() as db:
        rows = db.execute("SELECT * FROM menu_items ORDER BY id").fetchall()
    return jsonify([dict(row) for row in rows])


@app.post("/api/orders")
def create_order():
    data = request.get_json(silent=True) or {}
    student_name = str(data.get("student_name", "")).strip()
    pickup_time = str(data.get("pickup_time", "")).strip()
    pickup_place = str(data.get("pickup_place", "")).strip()
    cart = data.get("items", [])

    if not student_name or not pickup_time or not pickup_place:
        return jsonify(error="Name, pickup time, and pickup place are required."), 400
    if not isinstance(cart, list) or not cart:
        return jsonify(error="Your cart is empty."), 400

    quantities = {}
    try:
        for entry in cart:
            item_id = int(entry["id"])
            quantity = int(entry["quantity"])
            if quantity < 1 or quantity > 20:
                raise ValueError
            quantities[item_id] = quantities.get(item_id, 0) + quantity
    except (KeyError, TypeError, ValueError):
        return jsonify(error="The cart contains an invalid item or quantity."), 400

    with get_db() as db:
        placeholders = ",".join("?" for _ in quantities)
        rows = db.execute(
            f"SELECT * FROM menu_items WHERE id IN ({placeholders})",
            list(quantities.keys())
        ).fetchall()
        by_id = {row["id"]: row for row in rows}
        if len(by_id) != len(quantities):
            return jsonify(error="One or more menu items no longer exist."), 400
        if any(not by_id[item_id]["available"] for item_id in quantities):
            return jsonify(error="One or more items are currently unavailable."), 409

        total = sum(by_id[item_id]["price"] * qty for item_id, qty in quantities.items())
        cursor = db.execute(
            """INSERT INTO orders (student_name, pickup_time, pickup_place, total)
               VALUES (?, ?, ?, ?)""",
            (student_name, pickup_time, pickup_place, total)
        )
        order_id = cursor.lastrowid
        for item_id, quantity in quantities.items():
            item = by_id[item_id]
            db.execute(
                """INSERT INTO order_items
                   (order_id, menu_item_id, item_name, quantity, unit_price)
                   VALUES (?, ?, ?, ?, ?)""",
                (order_id, item_id, item["name"], quantity, item["price"])
            )

    return jsonify(message="Order placed successfully.", order_id=order_id, total=round(total, 2)), 201


@app.get("/api/orders")
def list_orders():
    with get_db() as db:
        orders = db.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
        result = []
        for order in orders:
            items = db.execute(
                "SELECT item_name, quantity, unit_price FROM order_items WHERE order_id = ?",
                (order["id"],)
            ).fetchall()
            result.append({**dict(order), "items": [dict(item) for item in items]})
    return jsonify(result)


@app.patch("/api/orders/<int:order_id>/status")
def update_order_status(order_id):
    data = request.get_json(silent=True) or {}
    status = data.get("status")
    allowed = {"Preparing", "Ready", "Completed"}
    if status not in allowed:
        return jsonify(error="Choose Preparing, Ready, or Completed."), 400
    with get_db() as db:
        cursor = db.execute(
            "UPDATE orders SET status = ? WHERE id = ?", (status, order_id)
        )
        if cursor.rowcount == 0:
            return jsonify(error="Order not found."), 404
    return jsonify(message="Order status updated.", status=status)


@app.patch("/api/menu/<int:item_id>/availability")
def update_availability(item_id):
    data = request.get_json(silent=True) or {}
    available = data.get("available")
    if not isinstance(available, bool):
        return jsonify(error="Availability must be true or false."), 400
    with get_db() as db:
        cursor = db.execute(
            "UPDATE menu_items SET available = ? WHERE id = ?",
            (int(available), item_id)
        )
        if cursor.rowcount == 0:
            return jsonify(error="Menu item not found."), 404
    return jsonify(message="Availability updated.")


# Initialize the database whether the app is started with `python app.py`
# or with the Flask CLI (`flask --app app run`).
init_db()

if __name__ == "__main__":
    app.run(debug=True)
