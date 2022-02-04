
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aee795742a1'
down_revision = 'fdbcafe5beec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts2', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="Posts2", referent_table="Users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="Posts2")
    op.drop_column('Posts2', 'owner_id')
    pass
