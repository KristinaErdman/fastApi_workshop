"""create operation

Revision ID: 047d6478390c
Revises: 
Create Date: 2022-09-21 23:24:36.773341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '047d6478390c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('kind', sa.String(), nullable=True),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations')
    # ### end Alembic commands ###
