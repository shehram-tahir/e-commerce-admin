from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas import InventoryResponse
from typing import List


router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/", response_model=List[InventoryResponse])
def get_inventory(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Inventory).offset(skip).limit(limit).all()


@router.get("/low-stock", response_model=List[InventoryResponse])
def low_stock(db: Session = Depends(get_db)):
    return db.query(models.Inventory).filter(models.Inventory.quantity < models.Inventory.low_stock_threshold).all()


@router.put("/{product_id}", response_model=InventoryResponse)
def update_inventory(product_id: int, quantity: int, db: Session = Depends(get_db)):
    inventory = db.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory.quantity = quantity
    db.commit()
    db.refresh(inventory)
    return inventory
