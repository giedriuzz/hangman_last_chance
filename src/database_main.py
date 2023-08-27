"""Module for database data manipulation"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Union

from db_direct import SqlDatabase


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

    def add_round(
        self,
        game_id: int,
        word: str,
        guess_time: datetime,
        hanged: bool,
        guesses_made: int,
        user_id: int,
    ) -> None:
        """Add round"""
        self.base.add_game_to_db(
            game_id=game_id,
            word=word,
            guess_time=guess_time,
            hanged=hanged,
            guesses_made=guesses_made,
            user_id=user_id,
        )

    def get_game_info(self, game_id: int) -> tuple:
        """Get game info"""
        game = self.base.get_game_info_by_game_id(game_id=game_id)

        return (
            f"\nGame date: {game[0][0].date()}",
            f"\nGamed time: {game[1]}",
            f"\nGames wined: {game[2]}",
            f"\nGames lost: {game[3]}",
        )


if __name__ == "__main__":
    mng = DatabaseIntermediate("hangman")

    print(*mng.get_game_info(1693159639))
