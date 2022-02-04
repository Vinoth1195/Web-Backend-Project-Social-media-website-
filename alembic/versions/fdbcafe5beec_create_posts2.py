"""create Posts2

Revision ID: fdbcafe5beec
Revises: 
Create Date: 2022-02-02 19:47:14.096427

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fdbcafe5beec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Posts2',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Posts2_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('published', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Posts2_pkey')
    )
    # #
    pass


def downgrade():
    op.drop_table('Posts2')
    pass
