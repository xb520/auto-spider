"""empty message

Revision ID: 44c32f3104ca
Revises: 
Create Date: 2018-11-21 17:38:00.759947

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '44c32f3104ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ms_images')
    op.drop_table('ms_video_resource')
    op.drop_table('ms_subtitles')
    op.drop_table('ms_cast_member')
    op.drop_index('ms_genres_un', table_name='ms_genres')
    op.drop_table('ms_genres')
    op.drop_table('ms_video')
    op.drop_index('ms_video_genres_un', table_name='ms_video_genres')
    op.drop_table('ms_video_genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ms_video_genres',
    sa.Column('videoid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('genreid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['genreid'], ['ms_genres.id'], name='ms_video_genres_ms_genres_fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['videoid'], ['ms_video.id'], name='ms_video_genres_ms_video_fk', ondelete='CASCADE'),
    mysql_comment='媒体类型关联表',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ms_video_genres_un', 'ms_video_genres', ['videoid', 'genreid'], unique=True)
    op.create_table('ms_video',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('alias', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('year', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('duration', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('score', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('region', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('imdbid', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_comment='视频资源',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('ms_genres',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('alias', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_comment='媒体分类',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ms_genres_un', 'ms_genres', ['name'], unique=True)
    op.create_table('ms_cast_member',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('role', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('videoid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['videoid'], ['ms_video.id'], name='ms_cast_member_ms_video_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_comment='演职人员表',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('ms_subtitles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('url', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('language', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('ftype', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('videoid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['videoid'], ['ms_video.id'], name='ms_subtitles_ms_video_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_comment='视频字幕',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('ms_video_resource',
    sa.Column('id', mysql.INTEGER(display_width=11), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
    sa.Column('url', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('resolution', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('bitrate', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('codec', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('videoid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['videoid'], ['ms_video.id'], name='ms_video_resource_ms_video_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_comment='媒体资源',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('ms_images',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('url', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('resolution', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('videoid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['videoid'], ['ms_video.id'], name='ms_images_ms_video_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_comment='媒体图片库',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
