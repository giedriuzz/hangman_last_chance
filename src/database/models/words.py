from db.base import Base
from sqlalchemy import Column, Integer, String


class Words(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True)
    word = Column("word", String)
    category = Column("category", String)
    difficulty = Column("difficulty", Integer)
