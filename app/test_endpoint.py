from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_sales():
    response = client.get("/sales/?skip=0&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5


def test_filter_sales_by_product():
    response = client.get("/sales/filter?product_id=1&limit=3")
    assert response.status_code == 200
    assert all(sale["product_id"] == 1 for sale in response.json())


def test_sales_summary():
    response = client.get("/sales/summary")
    assert response.status_code == 200
    data = response.json()
    for key in ["daily", "weekly", "monthly", "yearly"]:
        assert key in data
        assert isinstance(data[key], (int, float))

def test_get_inventory():
    response = client.get("/inventory/?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 10


def test_get_low_stock_inventory():
    response = client.get("/inventory/low-stock?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_inventory():
    product_id = 1
    new_quantity = 42
    response = client.put(f"/inventory/{product_id}?quantity={new_quantity}")
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == product_id
    assert data["quantity"] == new_quantity
