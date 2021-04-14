"""Initial migration.

Revision ID: 00dec7abb2ea
Revises:
Create Date: 2021-04-14 21:07:34.310292

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
# flake8: noqa
# revision identifiers, used by Alembic.
revision = '00dec7abb2ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_weather_city_name', table_name='weather')
    op.drop_index('ix_weather_main', table_name='weather')
    op.drop_index('ix_weather_temperature', table_name='weather')
    op.drop_index('ix_weather_time', table_name='weather')
    op.drop_table('weather')
    op.drop_table('service')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('url', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('weather',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('service_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('city_name', mysql.VARCHAR(collation='utf8_unicode_ci', length=80), nullable=True),
    sa.Column('country', mysql.VARCHAR(collation='utf8_unicode_ci', length=5), nullable=True),
    sa.Column('latitude', mysql.FLOAT(), nullable=True),
    sa.Column('longitude', mysql.FLOAT(), nullable=True),
    sa.Column('main', mysql.VARCHAR(collation='utf8_unicode_ci', length=20), nullable=True),
    sa.Column('description', mysql.VARCHAR(collation='utf8_unicode_ci', length=40), nullable=True),
    sa.Column('clouds', mysql.FLOAT(), nullable=True),
    sa.Column('temperature', mysql.FLOAT(), nullable=True),
    sa.Column('temp_min', mysql.FLOAT(), nullable=True),
    sa.Column('temp_max', mysql.FLOAT(), nullable=True),
    sa.Column('pressure', mysql.FLOAT(), nullable=True),
    sa.Column('humidity', mysql.FLOAT(), nullable=True),
    sa.Column('wind_speed', mysql.FLOAT(), nullable=True),
    sa.Column('wind_deg', mysql.FLOAT(), nullable=True),
    sa.Column('time', mysql.VARCHAR(collation='utf8_unicode_ci', length=30), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], name='weather_ibfk_1', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_weather_time', 'weather', ['time'], unique=False)
    op.create_index('ix_weather_temperature', 'weather', ['temperature'], unique=False)
    op.create_index('ix_weather_main', 'weather', ['main'], unique=False)
    op.create_index('ix_weather_city_name', 'weather', ['city_name'], unique=False)
    # ### end Alembic commands ###
