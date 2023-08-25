from datetime import datetime, time
from typing import Optional, Union, List

from models.user import User
from models.words import Words
from models.game import Game
from db.base import Base

from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, SQLAlchemyError  # for error handling
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta


class SqliteDatabase:
    def __init__(self, filename: str = "") -> None:
        self.filename = filename
        self.engine = create_engine(f"sqlite:///{self.filename}.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_database(self):
        """Creates database if it does not exist"""
        Base.metadata.create_all(self.engine, checkfirst=True)

    def register_user(self, name: str, surname: str, email: str, passwd: str) -> None:
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

    def get_user_by_email(self, user_email: str) -> User | bool:
        """
        Args:
            user_email (str): _description_
        Get user from base.
        function check is user email is unique
        """
        user = self.session.query(User).filter_by(email=user_email).one()
        if user:
            return user
        return False

    def get_game_by_user_id(self, user_id: int) -> Game | bool:
        """
        Args:
            user_id (int): user id number
        Get games by user id from base.
        """
        game = self.session.query(Game).filter_by(user_id=user_id).one()
        if game:
            return game
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
        self, category: str, difficulty: int
    ) -> list:
        """
        Args:
            category (str): _description_
            difficulty (int): _description_
        Get words by category and difficulty from base.
        """
        words = self.session.query(Words).filter_by(category=category).all()
        words_list: list = []
        for word in words:
            word_lenght = int(word.difficulty)
            if difficulty == 1:
                if word_lenght <= 4:
                    words_list.append(word.word)
                continue
            if difficulty == 2:
                if word_lenght >= 5 and word_lenght <= 7:
                    words_list.append(word.word)
                continue
            if difficulty == 3:
                if word_lenght >= 8:
                    words_list.append(word.word)
                continue
        return words_list

    def get_words_category(self) -> list:
        """
        Get words category from base.
        """
        words = self.session.query(Words).all()
        words_list: list = []
        for word in words:
            words_list.append(word.category)
        return set(words_list)


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

#     def create_task(
#         self,
#         user_email: str = "",
#         task_name: str = "",
#         task_note: str = "",
#     ) -> None:
#         by_user_email = (
#             self.session.query(User).filter_by(user_email=user_email).first()
#         )

#         task = Task(
#             task_name=task_name,
#             task_note=task_note,
#             task_id=by_user_email.id,  # type:ignore #!
#         )
#         user_one = self.session.query(User).get(by_user_email.id)  # type:ignore #!

#         user_one.tasks.append(task)
#         self.session.commit()

#     def get_tasks_by_user(self, user_email: str) -> list:
#         get_user = self.session.query(User).filter_by(user_email=user_email).first()
#         tasks = (
#             self.session.query(Task).filter_by(task_id=get_user.id).all()
#         )  #! #type:ignore
#         tasks_id: list = []
#         for n in get_user.tasks:  # type:ignore
#             print(
#                 n.id,
#                 "  ",
#                 n.task_name,
#                 n.task_note,
#                 n.task_create_date,
#                 n.task_finish_date,
#                 n.task_status,
#             )
#             tasks_id.append(n.id)
#         return tasks_id

#     def change_task(
#         self,
#         task_id: int,
#         task_name: str,
#         task_note: str,
#         task_finished: datetime,
#         task_status: str,
#     ) -> None:
#         user_task = self.session.query(Task).get(task_id)
#         user_task.task_name = task_name
#         user_task.task_note = task_note
#         user_task.task_finish_date = task_finished
#         user_task.task_status = task_status
#         self.session.commit()

# * pirmą kartą sukuriant db, užkomentuoti šitą eilutę
# database = SqliteDatabase(filename="hangman")
# database.create_database()

if __name__ == "__main__":
    # print(database.get_user(user_email="romas@lts.lt"))
    database = SqliteDatabase(filename="hangman")
    # database.register_user(
    #     name="Romas", surname="Romas", email="kgiedrius@namas.lt", passwd="123"
    # )
    user = database.get_user_by_email(user_email="kgiedrius@namas.lt")
    print(dir(user))

    print(database.get_words_category())

    print(
        database.get_words_by_category_and_difficulty(category="animals", difficulty=3)
    )
