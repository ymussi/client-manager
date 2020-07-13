"""create-table-product

Revision ID: ddec705864e8
Revises: a3008b051c45
Create Date: 2020-07-12 14:29:34.634972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddec705864e8'
down_revision = 'a3008b051c45'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('brand', sa.String(244), nullable=False),
                    sa.Column('title', sa.String(244), nullable=False, unique=True),
                    sa.Column('image', sa.String(2048), nullable=False),
                    sa.Column('price', sa.NUMERIC(), nullable=False),
                    sa.Column('reviewScore', sa.String(244), nullable=False),
                    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))


def downgrade():
    op.drop_table('product')
