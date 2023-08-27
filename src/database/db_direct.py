"""Module for database connection and data manipulation"""

from datetime import datetime
from typing import List, Union

from database.db.db_base import Base
from database.models.game import Game
from database.models.user import User
from database.models.words import Words
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


class SqlDatabase:
    """Class for database connection and data manipulation"""

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.engine = create_engine(f"sqlite:///{self.db_name}.db")
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def create_database(self):
        """Creates database if it does not exist"""
        Base.metadata.create_all(self.engine, checkfirst=True)

    def add_user_to_db(self, name: str, surname: str, email: str, passwd: str) -> None:
        """_summary_

        Args:
            name (str): _description_
            surname (str): _description_
            email (str): _description_
            passwd (str): _description_
        """ """"""

        user = User(
            name=name,
            surname=surname,
            email=email,
            passwd=passwd,
        )
        self.session.add(user)
        self.session.commit()

    def add_game_to_db(
        self,
        game_id: str,
        word: str,
        guess_time: datetime,
        hanged: bool,
        guesses_made: int,
        user_id: int,
    ) -> None:
        """Add each game to database
        Args:
            game_id (str): _description_
            word (str): _description_
            guess_time (datetime): calculated by game
            hanged (bool): _description_
            guesses_made (int): _description_
            user_id (int): _description_
        """
        game = Game(
            game_id=game_id,
            word=word,
            guess_time=guess_time,
            hanged=hanged,
            guesses_made=guesses_made,
            user_id=user_id,
        )
        self.session.add(game)
        self.session.commit()

    def get_user_by_email(self, user_email: str) -> Union[User, bool]:
        """
        Args:
            user_email (str): _description_
        Get user from base.
        function check is user email is unique
        """
        try:
            user = self.session.query(User).filter_by(email=user_email).one()
            if user:
                return user
        except NoResultFound:
            return False

    def user_games_by_user_id(self, user_id: int) -> Union[Game, bool]:
        """
        Args:
            user_id (int): user id number
        Get games by user id from base.
        """
        try:
            games = self.session.query(Game).filter_by(user_id=user_id).all()
            games_id: list = []
            for game in games:
                games_id.append(game.id)
            return games_id
        except NoResultFound:
            return False

    def add_words_in_table(self, category: str, *words) -> None:
        """
        Args:
            words (*args): _description_
            category (str): _description_
        """
        for word in words:
            word_difficulty = len(word)
            add_word = Words(
                word=word.upper(), category=category.lower(), difficulty=word_difficulty
            )
            self.session.add(add_word)
            self.session.commit()

    def get_words_by_category_and_difficulty(
        self, set_category: str, difficulty: list
    ) -> List[str]:
        """
        Args:
            category (str): _description_
            difficulty (list): _description_
        Get words by category and difficulty from base.
        """
        starts: int = difficulty[0]
        ends: int = difficulty[1]
        words_by_category = []
        my_filter = self.session.query(Words).filter_by(category=set_category).all()

        for word in my_filter:
            if starts <= int(word.difficulty) <= ends:
                words_by_category.append(word.word)
        return words_by_category

    def get_words_by_category(self, category: str) -> list:
        """
        Args:
            category (str): _description_
        Get words by category from base.
        """
        words = self.session.query(Words).filter_by(category=category).all()
        words_list: list = []
        for word in words:
            words_list.append(word.word)
        return words_list

    def get_words_category(self) -> list:
        """
        Get unique words category from base.
        """
        words = self.session.query(Words).distinct().all()
        categories_list: list = []
        for word in words:
            categories_list.append(word.category)
        return set(categories_list)

    def get_values_from_table_words(self) -> list:
        """
        Get words from base.
        """
        words = self.session.query(Words).all()
        words_list: list = []
        for word in words:
            words_list.append(word.word)
        return words_list


#     def get_users(self) -> list[int]:
#         users = self.session.query(User).all()
#         user_ids: list = []
#         print("ID")
#         for user in users:
#             user_ids.append(user.id)
#         return user_ids

#     def delete_user(self, user_id: int) -> None:
#         user = self.session.query(User).get(user_id)
#         self.session.delete(user)
#         self.session.commit()

#     def delete_user_task(self, task_id: int) -> None:
#         task = self.session.query(Task).get(task_id)
#         self.session.delete(task)
#         self.session.commit()

#     def check_password(self, users_email: str, user_passwd: str) -> bool:
#         self.users_email = users_email
#         try:
#             by_user_email = (
#                 self.session.query(User).filter_by(user_email=self.users_email).first()
#             )
#             if by_user_email.user_passwd == user_passwd:  # type:ignore #!
#                 return True
#             else:
#                 return False

#         except:
#             return False


# * pirmą kartą sukuriant db, užkomentuoti šitą eilutę
# database = SqlDatabase(filename="hangman")
# database.create_database()

if __name__ == "__main__":
    pass
