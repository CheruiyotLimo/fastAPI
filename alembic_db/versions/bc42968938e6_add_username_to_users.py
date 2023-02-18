"""add username to users

Revision ID: bc42968938e6
Revises: d3bc43f58293
Create Date: 2023-02-18 16:17:12.368848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc42968938e6'
down_revision = 'd3bc43f58293'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("username", sa.String(), nullable=False))


def downgrade() -> None:
    # op.drop_constraint("username", "users")
    op.drop_column("users", "username")
    pass
