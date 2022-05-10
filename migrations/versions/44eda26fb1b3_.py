"""empty message

Revision ID: 44eda26fb1b3
Revises: 7f92575375bd
Create Date: 2022-05-09 23:32:48.780941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44eda26fb1b3'
down_revision = '7f92575375bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Stars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('galaxy', sa.String(length=120), nullable=False),
    sa.Column('mass', sa.String(length=120), nullable=False),
    sa.Column('shine_color', sa.String(length=120), nullable=False),
    sa.Column('distance_from_sun', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('distance_from_sun'),
    sa.UniqueConstraint('distance_from_sun'),
    sa.UniqueConstraint('galaxy'),
    sa.UniqueConstraint('galaxy'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('shine_color'),
    sa.UniqueConstraint('shine_color')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Stars')
    # ### end Alembic commands ###