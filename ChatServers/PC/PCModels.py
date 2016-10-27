# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Pachongimage(Base):
    __tablename__ = 'pachongimage'

    id = Column(Integer, primary_key=True)
    imgaddress = Column(String(255))
    imgtitle = Column(String(255))
    imgfromurl = Column(String(255))


class Rgperson(Base):
    __tablename__ = 'rgperson'

    id = Column(Integer, primary_key=True)
    name = Column(String(12))
    age = Column(Integer)
    sports = Column(String(255))
    height = Column(Integer)
