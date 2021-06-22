from fastapi import APIRouter

from bsl.routes import balance, healthchek

api_router = APIRouter()

api_router.include_router(balance.router, tags=["balance"])
api_router.include_router(healthchek.router, tags=["healthchek"])
