"""Module for database tables"""

import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    create_engine,
    Table,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///hangman.db")
Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("game_id", Integer, ForeignKey("game.id")),
)


class User(Base):
    """Table for user information"""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String, unique=True)
    passwd = Column("Passwd", String)
    created_date = Column("Creation_date", DateTime, default=datetime.datetime.utcnow)
    games = relationship("Game", secondary=association_table, back_populates="users")


class Game(Base):
    """Table for game information"""

    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    word = Column("Word", String)
    guessing_starting_time = Column(
        "Guessing started", DateTime, default=datetime.datetime.utcnow
    )
    guessing_stopped_time = Column(
        "Guessing finished", DateTime, default=datetime.datetime.utcnow
    )
    time_for_guessing = Column("Time spend", DateTime, default=datetime.datetime.utcnow)
    hanged = Column("Hanged", Boolean)
    guessed_letters = Column("Guessed letters", String)
    not_guessed_letters = Column("Not guessed letters", String)
    attempts = Column("Attempts", String)
    users = relationship("User", secondary=association_table, back_populates="games")
    word = relationship("Word", back_populates="game")


class Word(Base):
    """Table for word information"""

    __tablename__ = "word"
    id = Column(Integer, primary_key=True)
    word = Column("Word", String, unique=True)
    word_id = Column("Word Id", Integer, ForeignKey("game.id"))
    game = relationship("Game", back_populates="word")


Base.metadata.create_all(engine)
