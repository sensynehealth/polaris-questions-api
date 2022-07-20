"""empty message

Revision ID: aa5f5c5f495f
Revises: 8c883df631cd
Create Date: 2018-03-15 10:10:29.647887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa5f5c5f495f'
down_revision = '8c883df631cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('declined', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey', 'declined')
    # ### end Alembic commands ###
