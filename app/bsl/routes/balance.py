from fastapi import APIRouter, Depends
from starlette import status

from bsl.schemas import MainMessage, StatusMessage, UpdateBalanceMessage
from bsl.core import database
from bsl.models import users as user_model
from bsl.utils import get_current_user

router = APIRouter()


@router.post("/status", response_model=MainMessage, status_code=status.HTTP_200_OK)
async def get_status(
        req: StatusMessage,
        user: user_model = Depends(get_current_user),
):
    return {
        'addition': user,
        'status': status.HTTP_200_OK,
        'result': True,
    }


@router.post("/add", response_model=MainMessage, status_code=status.HTTP_200_OK)
async def add_balance(
        req: UpdateBalanceMessage,
        user: user_model = Depends(get_current_user),
):
    if not user['status']:
        return {
            'addition': user,
            'status': status.HTTP_200_OK,
            'result': False,
        }

    query = (
        user_model
            .update()
            .where(user_model.c.uuid == user['uuid'])
            .values(balance=req.addition.balance + user['balance'])
            .returning(
                user_model.c.uuid,
                user_model.c.name,
                user_model.c.balance,
                user_model.c.holds,
                user_model.c.status,
            )
    )

    new_user = await database.fetch_one(query)

    return {
        'addition': new_user,
        'status': status.HTTP_200_OK,
        'result': True,
    }


@router.post("/substract", response_model=MainMessage, status_code=status.HTTP_200_OK)
async def substract_balance(
        req: UpdateBalanceMessage,
        user: user_model = Depends(get_current_user),
):

    new_balance = user['balance'] - user['holds'] - req.addition.balance
    if new_balance < 0:
        return {
            'addition': user,
            'status': status.HTTP_200_OK,
            'result': False,
        }

    query = (
        user_model
            .update()
            .where(user_model.c.uuid == user['uuid'])
            .values(holds=req.addition.balance + user['holds'])
            .returning(
                user_model.c.uuid,
                user_model.c.name,
                user_model.c.balance,
                user_model.c.holds,
                user_model.c.status,
            )
    )

    new_user = await database.fetch_one(query)

    return {
        'addition': new_user,
        'status': status.HTTP_200_OK,
        'result': True,
    }
