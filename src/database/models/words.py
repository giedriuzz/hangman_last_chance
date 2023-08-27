"""Model for the words table in the database"""

from database.db.db_base import Base
from sqlalchemy import Column, Integer, String


class Words(Base):
    """Class for words table in database"""

    __tablename__ = "words"
    id = Column(Integer, primary_key=True)
    word = Column("word", String, unique=True)
    category = Column("category", String)
    difficulty = Column("difficulty", Integer)
