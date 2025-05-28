from pydantic import BaseModel
from datetime import date
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    category_id: int

    class Config:
        orm_mode = True


class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    total_amount: float
    sale_date: Optional[date] = None


class InventoryCreate(BaseModel):
    product_id: int
    quantity: int
    low_stock_threshold: Optional[int] = 10


class SaleBase(BaseModel):
    product_id: int
    quantity: int
    total_amount: float
    sale_date: date


class SaleResponse(SaleBase):
    id: int
    class Config:
        orm_mode = True


class InventoryBase(BaseModel):
    product_id: int
    quantity: int


class InventoryResponse(InventoryBase):
    low_stock_threshold: int
    last_updated: Optional[date]
    class Config:
        orm_mode = True
