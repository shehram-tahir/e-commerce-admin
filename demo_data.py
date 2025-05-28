from app.database import SessionLocal
from app import models
from datetime import date, timedelta
import random

db = SessionLocal()

# Sample Categories
categories = ["Electronics", "Books", "Clothing"]
category_objs = [models.Category(name=name) for name in categories]
db.add_all(category_objs)
db.commit()

# Refresh created categories to get DB IDs
db.refresh(category_objs[0])
db.refresh(category_objs[1])
db.refresh(category_objs[2])

# Sample Products
products = [
    {"name": "Wireless Mouse", "price": 29.99, "category": category_objs[0]},
    {"name": "Laptop", "price": 999.99, "category": category_objs[0]},
    {"name": "Sci-fi Novel", "price": 15.50, "category": category_objs[1]},
    {"name": "T-shirt", "price": 10.00, "category": category_objs[2]},
]
product_objs = []
for sample_product in products:
    product = models.Product(
        description=f"Product Name: {sample_product['name']}",
        **sample_product
    )
    db.add(product)
    product_objs.append(product)

db.commit()

# Refresh product IDs
for product in product_objs:
    db.refresh(product)

# 3. Seed inventory
inventory_objs = []
for product in product_objs:
    inventory = models.Inventory(
        product_id=product.id,
        quantity=random.randint(5, 100),
        low_stock_threshold=10
    )
    inventory_objs.append(inventory)

db.add_all(inventory_objs)
db.commit()

# Sample Sales Data
today = date.today()
sales_objs = []
for product in product_objs:
    for i in range(10):  # 10 sales per product
        quantity = random.randint(1, 5)
        sale = models.Sale(
            product_id=product.id,
            quantity=quantity,
            total_amount=product.price * quantity,
            sale_date=today - timedelta(days=random.randint(1, 30))
        )
        sales_objs.append(sale)

db.add_all(sales_objs)
db.commit()

print("Sample data seeded successfully.")
