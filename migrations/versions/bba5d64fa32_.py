"""empty message

Revision ID: bba5d64fa32
Revises: 54fc9c08c874
Create Date: 2015-05-07 21:05:01.393695

"""

# revision identifiers, used by Alembic.
revision = 'bba5d64fa32'
down_revision = '54fc9c08c874'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('github_access_token', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###