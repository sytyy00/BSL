from fastapi import APIRouter

from bsl.routes import balance

api_router = APIRouter()

api_router.include_router(balance.router, tags=["balance"])
