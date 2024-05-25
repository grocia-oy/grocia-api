from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
