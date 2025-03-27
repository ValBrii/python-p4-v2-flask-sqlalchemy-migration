"""add Department

Revision ID: 659e4cb30304
Revises: b90941afb98c
Create Date: 2025-03-27 11:25:32.608089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '659e4cb30304'
down_revision = 'b90941afb98c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
