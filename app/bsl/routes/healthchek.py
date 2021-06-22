from fastapi import APIRouter, Response
from starlette import status

from bsl.core import RedisChecker, DatabaseChecker

router = APIRouter()


@router.get("/ping", status_code=status.HTTP_204_NO_CONTENT)
async def health():
    if all([await RedisChecker().check(), await DatabaseChecker().check()]):
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
