"""create alembic_test_table

Revision ID: 99667bbc468d
Revises: 
Create Date: 2023-08-27 22:27:44.983705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99667bbc468d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('AlembicTest', sa.Column("Id", sa.Integer(), nullable=False, primary_key=True, index=True),
                    sa.Column("Name", sa.String()))
    pass


def downgrade() -> None:
    op.drop_table('AlembicTest')
    pass
