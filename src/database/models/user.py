"""Module for user table in database"""
from database.db.db_base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    email = Column("email", String, unique=True)
    passwd = Column("password", String)
    games = relationship("Game", back_populates="users")

    @validates("email")
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("Failed simple email validation")
        return address
