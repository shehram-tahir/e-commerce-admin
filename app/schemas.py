from pydantic import BaseModel
from datetime import date
from typing import Optional


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
