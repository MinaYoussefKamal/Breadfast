import json
import app as cafeteria


def setup_function():
    cafeteria.app.config["TESTING"] = True
    cafeteria.DB_PATH = cafeteria.BASE_DIR / "test_cafeteria.db"
    cafeteria.init_db()


def teardown_function():
    cafeteria.DB_PATH.unlink(missing_ok=True)


def test_home_page_loads():
    response = cafeteria.app.test_client().get("/")
    assert response.status_code == 200
    assert b"Today's menu" in response.data


def test_menu_api_returns_items():
    response = cafeteria.app.test_client().get("/api/menu")
    assert response.status_code == 200
    assert len(response.get_json()) >= 1


def test_order_can_be_created_and_listed():
    client = cafeteria.app.test_client()
    menu = client.get("/api/menu").get_json()
    available = next(item for item in menu if item["available"])
    response = client.post("/api/orders", json={
        "student_name": "Test Student",
        "pickup_time": "12:30",
        "pickup_place": "Main Cafeteria",
        "items": [{"id": available["id"], "quantity": 2}]
    })
    assert response.status_code == 201
    order_id = response.get_json()["order_id"]
    orders = client.get("/api/orders").get_json()
    assert orders[0]["id"] == order_id


def test_order_rejects_empty_cart():
    response = cafeteria.app.test_client().post("/api/orders", json={
        "student_name": "Test Student",
        "pickup_time": "12:30",
        "pickup_place": "Main Cafeteria",
        "items": []
    })
    assert response.status_code == 400
