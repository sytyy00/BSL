from fastapi.exceptions import HTTPException
from starlette import status

from bsl.schemas import StatusMessage
from bsl.core import database
from bsl.models import users


async def get_current_user(req: StatusMessage):
    query = users.select().where(users.c.uuid == req.addition.uuid)
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
