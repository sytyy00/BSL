from sqlalchemy import Table, Integer, Column, Boolean, VARCHAR
from sqlalchemy.dialects.postgresql import UUID

from bsl.core import metadata

users = Table(
    'users',
    metadata,
    Column('uuid', UUID(), primary_key=True, index=True),
    Column('name', VARCHAR),
    Column('balance', Integer),
    Column('holds', Integer),
    Column('status', Boolean),
)
