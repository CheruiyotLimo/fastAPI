"""add content column to posts

Revision ID: abf011efc1f1
Revises: 42870e26f726
Create Date: 2023-02-15 15:12:37.013150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abf011efc1f1'
down_revision = '42870e26f726'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")