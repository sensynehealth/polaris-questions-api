"""empty message

Revision ID: f7af1fa592c6
Revises: 
Create Date: 2018-02-27 19:19:53.925980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7af1fa592c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('group', sa.String(), nullable=False),
                    sa.Column('deleted', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('answer',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('survey_id', sa.String(), nullable=False),
                    sa.Column('question_id', sa.String(), nullable=False),
                    sa.Column('answer', sa.String(), nullable=False),
                    sa.Column('deleted', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('question_option_type',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=False),
                    sa.Column('deleted', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('question_type',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=False),
                    sa.Column('deleted', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('question',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('question', sa.String(), nullable=False),
                    sa.Column('deleted', sa.DateTime(), nullable=True),
                    sa.Column('question_type_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['question_type_id'], [
                        'question_type.uuid'], ),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('survey',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('user_type', sa.String(), nullable=False),
                    sa.Column('user_id', sa.String(), nullable=False),
                    sa.Column('group_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['group_id'], ['group.uuid'], ),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    op.create_table('question_group',
                    sa.Column('question_id', sa.String(), nullable=False),
                    sa.Column('group_id', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['group_id'], ['group.uuid'], ),
                    sa.ForeignKeyConstraint(
                        ['question_id'], ['question.uuid'], ),
                    sa.PrimaryKeyConstraint('question_id', 'group_id')
                    )
    op.create_table('question_option',
                    sa.Column('uuid', sa.String(length=36), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('modified', sa.DateTime(), nullable=False),
                    sa.Column('text', sa.String(), nullable=False),
                    sa.Column('value', sa.String(), nullable=False),
                    sa.Column('order', sa.Integer(), nullable=False),
                    sa.Column('deleted', sa.DateTime(), nullable=True),
                    sa.Column('question_id', sa.String(), nullable=True),
                    sa.Column('question_option_type_id',
                              sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['question_id'], ['question.uuid'], ),
                    sa.ForeignKeyConstraint(['question_option_type_id'], [
                        'question_option_type.uuid'], ),
                    sa.PrimaryKeyConstraint('uuid')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_option')
    op.drop_table('question_group')
    op.drop_table('survey')
    op.drop_table('question')
    op.drop_table('question_type')
    op.drop_table('question_option_type')
    op.drop_table('answer')
    # ### end Alembic commands ###
