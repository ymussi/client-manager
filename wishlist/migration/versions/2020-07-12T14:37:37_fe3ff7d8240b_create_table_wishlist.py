"""create-table-wishlist

Revision ID: fe3ff7d8240b
Revises: ddec705864e8
Create Date: 2020-07-12 14:37:41.214430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe3ff7d8240b'
down_revision = 'ddec705864e8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('wishlist',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('client_id', sa.Integer(), sa.ForeignKey('customer.id'), nullable=False),
                    sa.Column('product_id', sa.Integer(), sa.ForeignKey('product.id'), nullable=False))
    op.create_unique_constraint('unique_wishlist', 'wishlist', ['client_id', 'product_id'])

def downgrade():
    op.drop_table('wishlist')
