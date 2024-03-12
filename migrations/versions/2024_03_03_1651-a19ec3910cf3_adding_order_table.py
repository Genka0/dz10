"""Adding order table

Revision ID: a19ec3910cf3
Revises: 7cd9ce3f9752
Create Date: 2024-03-03 16:51:33.835898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Ваша существующая логика миграции здесь

    # Используем функцию CASE для преобразования значений nickname в тип BOOLEAN
    op.execute("ALTER TABLE users ALTER COLUMN nickname TYPE BOOLEAN USING CASE WHEN nickname = 'true' THEN true ELSE false END")

# revision identifiers, used by Alembic.
revision: str = 'a19ec3910cf3'
down_revision: Union[str, None] = '7cd9ce3f9752'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('customer', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('addresses', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('addresses', sa.Column('notes', sa.String(), nullable=True))
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('money', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('notes', sa.String(), nullable=True))
    op.alter_column('users', 'nickname',
               existing_type=sa.VARCHAR(),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'nickname',
               existing_type=sa.Boolean(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.drop_column('users', 'notes')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'money')
    op.drop_column('users', 'age')
    op.drop_column('addresses', 'notes')
    op.drop_column('addresses', 'created_at')
    op.drop_table('orders')
    # ### end Alembic commands ###
