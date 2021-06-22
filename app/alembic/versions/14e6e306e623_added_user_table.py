"""Added user table

Revision ID: 14e6e306e623
Revises: 
Create Date: 2021-06-22 15:15:24.288192

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '14e6e306e623'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users_table = op.create_table('users',
                                  sa.Column('uuid', postgresql.UUID(), nullable=False),
                                  sa.Column('name', sa.VARCHAR(), nullable=True),
                                  sa.Column('balance', sa.Integer(), nullable=True),
                                  sa.Column('holds', sa.Integer(), nullable=True),
                                  sa.Column('status', sa.Boolean(), nullable=True),
                                  sa.PrimaryKeyConstraint('uuid')
                                  )
    op.create_index(op.f('ix_users_uuid'), 'users', ['uuid'], unique=False)
    # ### end Alembic commands ###

    users_data = [
        {
            'uuid': '26c940a1-7228-4ea2-a3bce6460b172040',
            'name': 'Петров Иван Сергеевич',
            'balance': 1700,
            'holds': 300,
            'status': True,
        },
        {
            'uuid': '7badc8f8-65bc-449a-8cde855234ac63e1',
            'name': 'Kazitsky Jason',
            'balance': 200,
            'holds': 200,
            'status': True,
        },
        {
            'uuid': '5597cc3d-c948-48a0-b711-393edf20d9c0',
            'name': 'Пархоменко Антон Александрович',
            'balance': 10,
            'holds': 300,
            'status': True,
        },
        {
            'uuid': '867f0924-a917-4711-939b90b179a96392',
            'name': 'Петечкин Петр Измаилович',
            'balance': 1000000,
            'holds': 1,
            'status': False,
        },
    ]

    op.bulk_insert(users_table, users_data)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_uuid'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###