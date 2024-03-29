"""add a relationship between a user and his comment

Revision ID: ee0ffec3442d
Revises: 9c94156375c5
Create Date: 2021-09-20 21:42:02.069629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee0ffec3442d'
down_revision = '9c94156375c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###
