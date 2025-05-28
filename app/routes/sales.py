from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app import models
from app.schemas import SaleResponse
from typing import List, Optional
from datetime import date, timedelta

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.get("/", response_model=List[SaleResponse])
def get_all_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Sale).offset(skip).limit(limit).all()


@router.get("/filter", response_model=List[SaleResponse])
def filter_sales(product_id: Optional[int] = None, category_id: Optional[int] = None,
                 start_date: Optional[date] = None, end_date: Optional[date] = None,
                 skip: int = 0, limit: int = 10,
                 db: Session = Depends(get_db)
):
    query = db.query(models.Sale)
    if product_id:
        query = query.filter(models.Sale.product_id == product_id)
    if start_date:
        query = query.filter(models.Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(models.Sale.sale_date <= end_date)
    if category_id:
        query = query.join(models.Product).filter(models.Product.category_id == category_id)
    return query.offset(skip).limit(limit).all()


@router.get("/summary")
def sales_summary(db: Session = Depends(get_db)):
    today = date.today()
    query = lambda start, end : db.query(models.Sale).filter(models.Sale.sale_date.between(start, end)
                                                             ).with_entities(func.sum(models.Sale.total_amount)
                                                                             ).scalar() or 0
    return {
        "daily": query(today, today),
        "weekly": query(today - timedelta(days=7), today),
        "monthly": query(today.replace(day=1), today),
        "yearly": query(today.replace(month=1, day=1), today)
    }
