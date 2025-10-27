"""add content column to posts table

Revision ID: 26e362fe6919
Revises: 1c41e9eff5fa
Create Date: 2025-10-27 01:21:49.005474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26e362fe6919'
down_revision: Union[str, Sequence[str], None] = '1c41e9eff5fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
