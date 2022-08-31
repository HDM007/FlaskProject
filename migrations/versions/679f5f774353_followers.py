"""followers

Revision ID: 679f5f774353
Revises: f621fa377a99
Create Date: 2022-07-29 02:03:36.618044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '679f5f774353'
down_revision = 'f621fa377a99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
