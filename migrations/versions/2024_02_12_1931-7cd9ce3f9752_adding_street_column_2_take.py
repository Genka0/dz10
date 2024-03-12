"""Adding street column 2 take

Revision ID: 7cd9ce3f9752
Revises: 7cda0b2d7d7c
Create Date: 2024-02-12 19:31:36.771549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

def upgrade():
    # Ваша существующая логика миграции здесь

    # Используем функцию CASE для преобразования значений nickname в тип BOOLEAN
    op.execute("ALTER TABLE users ALTER COLUMN nickname TYPE BOOLEAN USING CASE WHEN nickname = 'true' THEN true ELSE false END")


# revision identifiers, used by Alembic.
revision: str = '7cd9ce3f9752'
down_revision: Union[str, None] = '7cda0b2d7d7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
