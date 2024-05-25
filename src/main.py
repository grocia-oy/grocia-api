from fastapi import FastAPI

from src.products.route import router as products_router

from .config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


app.include_router(products_router, prefix=settings.API_V1_STR)
