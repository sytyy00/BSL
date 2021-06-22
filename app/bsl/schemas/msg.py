from typing import Dict
from uuid import UUID

from pydantic import BaseModel


class MainAddition(BaseModel):
    uuid: UUID
    balance: int
    name: str
    holds: int
    status: int


class MainMessage(BaseModel):
    addition: MainAddition
    description: Dict = None
    status: str
    result: bool


class StatusAddition(MainAddition):
    uuid: UUID
    balance: int = None
    name: str = None
    holds: int = None
    status: int = None


class StatusMessage(MainMessage):
    addition: StatusAddition
    status: str = None
    result: bool = None


class UpdateBalanceAddition(MainAddition):
    uuid: UUID
    balance: int
    name: str = None
    holds: int = None
    status: int = None


class UpdateBalanceMessage(MainMessage):
    addition: UpdateBalanceAddition
    status: str = None
    result: bool = None