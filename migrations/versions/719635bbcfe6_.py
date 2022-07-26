"""empty message

Revision ID: 719635bbcfe6
Revises: 15c9dbfaa09f
Create Date: 2018-03-05 15:35:25.842028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '719635bbcfe6'
down_revision = '15c9dbfaa09f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('text', sa.String(), nullable=True))
    op.add_column('answer', sa.Column('value', sa.String(), nullable=False))
    op.drop_column('answer', 'answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('answer', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('answer', 'value')
    op.drop_column('answer', 'text')
    # ### end Alembic commands ###
