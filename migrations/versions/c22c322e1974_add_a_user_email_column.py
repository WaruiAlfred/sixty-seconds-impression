"""add a user email column

Revision ID: c22c322e1974
Revises: b7aeac2370d7
Create Date: 2021-09-19 01:14:39.438337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c22c322e1974'
down_revision = 'b7aeac2370d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_user_email'), 'users', ['user_email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_email'), table_name='users')
    op.drop_column('users', 'user_email')
    # ### end Alembic commands ###