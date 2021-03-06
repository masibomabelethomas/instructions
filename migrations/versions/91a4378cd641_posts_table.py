"""posts table

Revision ID: 91a4378cd641
Revises: da3d69528287
Create Date: 2022-01-21 14:55:22.238283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91a4378cd641'
down_revision = 'da3d69528287'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['timestamp'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
