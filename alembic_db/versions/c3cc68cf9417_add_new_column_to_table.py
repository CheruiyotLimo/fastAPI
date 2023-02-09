"""add new column to table

Revision ID: c3cc68cf9417
Revises: 0c1c76ca76fc
Create Date: 2023-02-08 18:04:31.312470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3cc68cf9417'
down_revision = '0c1c76ca76fc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
