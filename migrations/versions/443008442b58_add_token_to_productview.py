"""Add token to ProductView

Revision ID: 443008442b58
Revises: 51c1d28297a6
Create Date: 2018-01-29 00:58:07.860865

"""

# revision identifiers, used by Alembic.
revision = '443008442b58'
down_revision = '51c1d28297a6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_view', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_view', schema=None) as batch_op:
        batch_op.drop_column('token')

    # ### end Alembic commands ###