"""added username column

Revision ID: 585bad0d9f81
Revises: bc42968938e6
Create Date: 2023-02-19 20:16:14.366155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '585bad0d9f81'
down_revision = 'bc42968938e6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
