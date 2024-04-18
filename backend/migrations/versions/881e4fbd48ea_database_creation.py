"""Database creation

Revision ID: 881e4fbd48ea
Revises: 
Create Date: 2024-04-10 12:25:20.414714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '881e4fbd48ea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subject')
    op.drop_table('role')
    op.drop_table('teacher_class')
    op.drop_table('student')
    op.drop_table('mark')
    op.drop_table('timetable')
    op.drop_table('class')
    op.drop_table('teacher')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('teacher_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('father_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='teacher_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='teacher_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('class',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('class_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='class_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('timetable',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('day_of_week', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('class_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('end_time', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], name='timetable_class_id_fkey'),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name='timetable_subject_id_fkey'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], name='timetable_teacher_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='timetable_pkey')
    )
    op.create_table('mark',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mark', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('set_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name='mark_student_id_fkey'),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name='mark_subject_id_fkey'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], name='mark_teacher_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='mark_pkey')
    )
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('father_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('class_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], name='student_class_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='student_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='student_pkey')
    )
    op.create_table('teacher_class',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('class_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], name='teacher_class_class_id_fkey'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], name='teacher_class_teacher_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='teacher_class_pkey')
    )
    op.create_table('role',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='role_pkey')
    )
    op.create_table('subject',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='subject_pkey')
    )
    # ### end Alembic commands ###
