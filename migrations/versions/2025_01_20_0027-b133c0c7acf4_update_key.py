"""Update key

Revision ID: b133c0c7acf4
Revises: 82bb06766c12
Create Date: 2025-01-20 00:27:47.477287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b133c0c7acf4'
down_revision: Union[str, None] = '82bb06766c12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'user_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=False)
    op.drop_constraint('messages_user_id_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_user_id_fkey', 'messages', 'users', ['user_id'], ['id'])
    op.alter_column('messages', 'user_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
