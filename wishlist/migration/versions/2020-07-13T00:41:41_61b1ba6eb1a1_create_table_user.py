"""create-table-user

Revision ID: 61b1ba6eb1a1
Revises: fe3ff7d8240b
Create Date: 2020-07-13 00:41:49.398404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b1ba6eb1a1'
down_revision = 'fe3ff7d8240b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('username', sa.String(244), nullable=False),
                    sa.Column('email', sa.String(244), nullable=False, unique=True),
                    sa.Column('password', sa.String(244), nullable=False),
                    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))


def downgrade():
    op.drop_table('user')
