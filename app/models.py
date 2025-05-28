from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric, Date, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category")
    inventory = relationship("Inventory", uselist=False, back_populates="product")
    sales = relationship("Sale", back_populates="product")

    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer, nullable=False)
    low_stock_threshold = Column(Integer, default=10)
    last_updated = Column(Date, server_default=func.now())

    product = relationship("Product", back_populates="inventory")


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="SET NULL"))
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    sale_date = Column(Date, nullable=False)
    created_at = Column(Date, server_default=func.now())

    product = relationship("Product", back_populates="sales")
