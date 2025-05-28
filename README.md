# 🛒 E-commerce Admin API – Backend Developer Task

This is a backend system built with **FastAPI** and **PostgreSQL** that powers an **admin dashboard** for managing an 
e-commerce platform. The system provides insights into sales, inventory, and supports product management operations.

---

## 🚀 Tech Stack

- **Python 3.9+**
- **FastAPI** – Web framework
- **SQLAlchemy** – ORM for database modeling
- **PostgreSQL** – Relational database
- **Uvicorn** – ASGI server
- **Pydantic** – Data validation
- **Pytest** – Unit testing

---

## 📦 How to Run?

Run the below commands to run the server, following the below instructions:

Update in .env file with the postgresql URL **DATABASE_URL** according to your DBMS:

- `pip3 install -r requirements.txt`

- `uvicorn main:app --reload`

To populate the database with dummy data, run the below command:
- `python demo_data.py`

These commands run the server at http://localhost:8000/

To the Swagger visit http://localhost:8000/docs


## 📦 Endpoints

### 📊 Inventory Module
- GET /inventory/
  - Retrieve all inventory records  
- GET /inventory/low-stock 
  - Get low stock inventories
- PUT /inventory/low-stock/{product_id} 
  - Update Inventory reord using the following data:
    - quantity

### 🏷️ Sales Module
- GET /sales/
  - Retrieve all sales records  
- GET /sales/filter/
  - Filter sales records by the following filters:
    - Product
    - Category
    - Date range
- GET /summary/
  - Get daily, weekly, monthly, and yearly summary of all sales

### 📌 Pagination
All list endpoints support pagination via:
- `skip`: number of records to skip
- `limit`: max records to return (default: 10)

---

## 🗃️ Database Schema

The system uses the following relational structure:

- `categories(id, name)`
- `products(id, name, description, price, category_id)`
- `inventory(id, product_id, quantity, low_stock_threshold, last_updated)`
- `sales(id, product_id, quantity, total_amount, sale_date)`

> ✅ Database normalization and indexing are applied.


