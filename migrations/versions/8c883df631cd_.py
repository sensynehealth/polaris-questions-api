"""empty message

Revision ID: 8c883df631cd
Revises: 719635bbcfe6
Create Date: 2018-03-06 08:19:35.391864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c883df631cd'
down_revision = '719635bbcfe6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('only_one_active_identical_question_option', 'answer', ['survey_id', 'question_id', 'value'], unique=True, postgresql_where=sa.text('deleted IS NULL'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('only_one_active_identical_question_option', table_name='answer')
    # ### end Alembic commands ###
