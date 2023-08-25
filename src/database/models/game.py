import datetime

from db.base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    game_id = Column("game", String)
    word = Column("word", String)
    guess_time = Column("guessing started", DateTime, default=datetime.datetime.utcnow)
    hanged = Column("hanged", Boolean)
    guesses_made = Column("guesses made", String)
    user_id = Column(Integer, ForeignKey("user.id"))
    users = relationship("User", back_populates="games")
