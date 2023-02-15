"""add foreign key to posts

Revision ID: f75116ccd27d
Revises: c9bb362b60c8
Create Date: 2023-02-15 15:31:30.078864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f75116ccd27d'
down_revision = 'c9bb362b60c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fkey", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_user_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
