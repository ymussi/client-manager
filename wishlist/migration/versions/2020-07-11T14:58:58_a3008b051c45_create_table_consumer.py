"""create-table-consumer

Revision ID: a3008b051c45
Revises: 
Create Date: 2020-07-11 14:58:06.491416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3008b051c45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('customer',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('name', sa.String(244), nullable=False),
                    sa.Column('email', sa.String(244), nullable=False, unique=True),
                    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))


def downgrade():
    op.drop_table('consumer')
