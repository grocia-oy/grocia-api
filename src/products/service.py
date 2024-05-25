import uuid

from sqlalchemy.orm import Session

from .models import DB_Product
from .schemas import ProductCreate


def get_all(db_session: Session):
    return db_session.query(DB_Product).all()


def create(db_session: Session, product_in: ProductCreate) -> DB_Product:
    db_product = DB_Product(**product_in.model_dump(), id=uuid.uuid4())

    db_session.add(db_product)
    db_session.commit()
    return db_product
