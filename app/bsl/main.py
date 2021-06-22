import asyncio
from fastapi import FastAPI
from huey import RedisHuey

from bsl.core import database, settings, psql_manager
from bsl.routes import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event("startup")
async def startup_event():
    await database.connect()


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await database.disconnect()


huey = RedisHuey(url=settings.REDIS_URL)


@huey.on_startup()
def open_db_connection():
    if not psql_manager.is_connection:
        psql_manager.connect()
