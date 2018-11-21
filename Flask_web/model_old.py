# coding: utf-8
from sqlalchemy import Column, ForeignKey, Index, String, Table, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MsGenre(Base):
    __tablename__ = 'ms_genres'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    alias = Column(String(200))

    ms_video = relationship('MsVideo', secondary='ms_video_genres')


class MsVideo(Base):
    __tablename__ = 'ms_video'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(500))
    alias = Column(String(500))
    description = Column(Text)
    year = Column(String(100))
    duration = Column(String(100))
    score = Column(String(100))
    region = Column(String(100))
    imdbid = Column(String(200))
    url = Column(String(500))


class MsCastMember(Base):
    __tablename__ = 'ms_cast_member'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(200), nullable=False)
    role = Column(String(100))
    videoid = Column(ForeignKey('ms_video.id', ondelete='CASCADE'), index=True)

    ms_video = relationship('MsVideo')


class MsImage(Base):
    __tablename__ = 'ms_images'

    id = Column(INTEGER(11), primary_key=True)
    url = Column(String(500), nullable=False)
    resolution = Column(String(100))
    videoid = Column(ForeignKey('ms_video.id', ondelete='CASCADE'), index=True)

    ms_video = relationship('MsVideo')


class MsSubtitle(Base):
    __tablename__ = 'ms_subtitles'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(100))
    url = Column(String(100))
    language = Column(String(100))
    ftype = Column(String(100))
    videoid = Column(ForeignKey('ms_video.id', ondelete='CASCADE'), nullable=False, index=True)

    ms_video = relationship('MsVideo')


t_ms_video_genres = Table(
    'ms_video_genres', metadata,
    Column('videoid', ForeignKey('ms_video.id', ondelete='CASCADE')),
    Column('genreid', ForeignKey('ms_genres.id', ondelete='CASCADE'), index=True),
    Index('ms_video_genres_un', 'videoid', 'genreid', unique=True)
)
