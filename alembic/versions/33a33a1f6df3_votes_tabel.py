"""VOTES tabel

Revision ID: 33a33a1f6df3
Revises: 800e2e5c015f
Create Date: 2022-02-03 11:31:58.881934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33a33a1f6df3'
down_revision = 'cb659287f4d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Posts2.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade():
    op.drop_table('Votes')
    pass
