

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '787d08f8188d'
down_revision = '0aee795742a1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Posts2', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('Posts2', sa.Column(
        'timestamp', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)

    pass


def downgrade():
    op.drop_column('Posts2', 'published')
    op.drop_column('Posts2', 'timestamp')
    pass
