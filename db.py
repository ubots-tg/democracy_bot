from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from secure import database_uri

engine = create_engine(database_uri)

Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    ruler = Column(String)
