"""Create USERS table

Revision ID: 0a3c396867b6
Revises: a2b8bcffc949
Create Date: 2022-02-04 17:59:51.529565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '0a3c396867b6'
down_revision = 'a2b8bcffc949'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Users_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Users_pkey'),
    sa.UniqueConstraint('email', name='Users_email_key')
    )
    op.add_column('Users', sa.Column('phone_number', sa.String(), nullable=True))

    op.add_column('Posts2', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="Posts2", referent_table="Users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="Posts2")
    op.drop_table('Users')
    op.drop_column('Posts2', 'owner_id')

    pass
