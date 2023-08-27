"""Module for database data manipulation"""

from abc import ABC, abstractmethod
from typing import Union

from database.db_direct import SqlDatabase
from database.models.user import User


class Abstract(ABC):
    """Blueprint for database data manipulation"""

    @abstractmethod
    def check_user_by_passwd_mail(self, user_passwd: str, user_email: str):
        """Check if user exists in database"""

    def get_games_by_user_id(self, user_id: int) -> list:
        """Get games by user id"""


class DatabaseIntermediate(Abstract):
    """Class for database data manipulation"""

    def __init__(self, db_name: str) -> None:
        self.base = SqlDatabase(db_name)

    def check_user_by_passwd_mail(
        self, user_passwd: str, user_email: str
    ) -> Union[tuple, bool]:
        """Check if user exists in database"""
        user = self.base.get_user_by_email(user_email=user_email)
        if user and user_passwd == user.passwd:
            return user.name, user.id
        return False

    def get_games_by_user_id(self, user_id: int) -> list:
        """Get games by user id"""
        games = self.base.user_games_by_user_id(user_id=user_id)
        games_id: list = []
        for game in games:
            games_id.append(game.id)
        return games_id

    def get_user_for_register(
        self, name: str, surname: str, email: str, passwd: str
    ) -> None:
        """Get user credentials for register"""
        self.base.add_user_to_db(
            name=name,
            surname=surname,
            email=email,
            passwd=passwd,
        )

    def get_words_by_category_difficulty(self, category: str, difficulty: int) -> list:
        """Get words by category and difficulty"""
        category = category.lower()
        if difficulty == 1:
            difficulty = (1, 4)
        if difficulty == 2:
            difficulty = (5, 8)
        if difficulty == 3:
            difficulty = (9, 12)
        words = self.base.get_words_by_category_and_difficulty(
            set_category=category, difficulty=(difficulty[0], difficulty[1])
        )
        return words

    def get_category(self) -> list:
        """Get category"""
        category = self.base.get_words_category()
        return [*category]


if __name__ == "__main__":
    mng = DatabaseIntermediate(db_name="hangman")
    # users = mng.check_user_by_passwd_mail(
    #     user_passwd="123", user_email="kgiedrius@namas.lt"
    # )
    # print(users)

    print(mng.get_words_by_category_difficulty(category="countries", difficulty=3))
