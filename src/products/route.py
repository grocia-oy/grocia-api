from typing import List

from fastapi import status
from fastapi.routing import APIRouter

from src.db import DbSession

from .schemas import Product, ProductCreate
from .service import create, get_all

router = APIRouter(prefix="/products", tags=["products"])


@router.get(
    "/",
    response_model=List[Product],
    response_description="Get all products",
    status_code=status.HTTP_200_OK,
)
async def get_products(db_session: DbSession):
    products = get_all(db_session)
    return products


@router.post(
    "/",
    response_model=Product,
    response_description="Create a new product",
    status_code=status.HTTP_201_CREATED,
)
async def create_product(db_session: DbSession, product: ProductCreate):
    db_product = create(db_session, product)
    return db_product
