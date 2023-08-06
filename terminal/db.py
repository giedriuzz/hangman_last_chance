"""Module for database tables"""

import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///projektai.db")
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String)
    passwd = Column("Passwd", String)
    created_date = Column("Creation_date", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"


Base.metadata.create_all(engine)
