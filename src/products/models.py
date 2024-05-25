from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from src.db import Base


class DB_Product(Base):
    __tablename__ = "products"

    id = Column(UUID, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )
    name = Column(String, nullable=False)
