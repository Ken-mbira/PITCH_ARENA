"""add a user email column

Revision ID: a73adce4827a
Revises: 890395ea388b
Create Date: 2021-09-17 14:20:19.992851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a73adce4827a'
down_revision = '890395ea388b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=100), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###