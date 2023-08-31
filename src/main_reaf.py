"""Module for game logic"""

import logging
import logging.config
from typing import Union

from termcolor import colored

from database.db_intermediate import DatabaseIntermediate
from inputs import input_email, input_passwd
from main import Categories, Letter
from validation import input_only_letters, return_dict_value_by_key


class Game:
    """Class for game methods"""

    logging.config.fileConfig(
        fname="logging.conf", disable_existing_loggers=False
    )  # noqa:E501

    def __init__(self, db_name) -> None:
        self.db_intermediate = DatabaseIntermediate(db_name)
        self.logger = logging.getLogger("sampleLogger")

    def registration(self) -> None:
        """Function for user registration"""
        print(
            f"\n{colored('              ', 'black', 'on_white', attrs=['bold'])}"
            f'{colored("Register","black", "on_white", attrs=["bold"])}'
            f'{colored("             ", "black", "on_white", attrs=["bold"])}'
        )

        name = input_only_letters(colored("\nName: ", "white", attrs=["bold"]))
        surname = input_only_letters(
            colored("Surname: ", "white", attrs=["bold"])
        )  # noqa: E501
        email, passwd = input_email(), input_passwd()
        if self.db_intermediate.read_user_by_mail(user_email=email) is False:
            self.db_intermediate.register_user(
                name=name, surname=surname, email=email, passwd=passwd
            )
            print(
                colored(
                    "You are registered. Now can login.",
                    "green",
                    attrs=["bold"],  # noqa:E501
                )  #
            )
        else:
            print(
                f'{colored("User with this email ","red", attrs=["bold"])}'
                f'{email}{colored(" already exists!", "red", attrs=["bold"])}'
            )

    def login(self) -> Union[bool, tuple[str]]:
        """Function for user login"""
        print(
            colored(
                "              Login                ",
                "black",
                "on_white",
                attrs=["bold"],
            ),
            "\n",
        )
        email, passwd = input_email(), input_passwd()
        user = self.db_intermediate.read_user_by_passwd_mail(
            user_passwd=passwd, user_email=email
        )
        if user is False:
            print(colored("User not found!", "red", attrs=["bold"]))
            return False
        name: str = user[0]
        user_id: str = user[1]
        print(
            f'{colored(name, "yellow", attrs=["bold"])}'
            f'{colored(" you are logged in!", "yellow", attrs=["bold"])}'
        )
        return name, user_id

    def category(self):
        """Method for get category"""

        categories = Categories(self.db_intermediate.get_category())
        categories_dict = categories.get_categories_enumerated()
        category = return_dict_value_by_key(
            len(categories_dict),
            categories.print_categories(categories_dict),
            categories_dict,
        )
        return category

    def clear_reload_list(self, letter_class: Letter) -> None:
        """Clear and reload lists in class Letter"""
        letter_class.LETTERS_LIST.clear()
        letter_class.reload_letters_list()
        letter_class.MATCHED_LETTERS.clear()
        letter_class.NOT_MATCHED_LETTERS.clear()
        letter_class.empty_word_list.clear()

    def starting_game(
        self, length: int, category, letter_class: Letter, guessing_word: str
    ) -> None:
        print(f'\n{colored("Round: ", "red")} {length}/10')
        print(colored("Category: ", "green"), category)
        print(colored("Letters left: ", "green"), *letter_class.LETTERS_LIST_TUPLE)
        print(
            colored("Guessing word: ", "blue", attrs=["bold"]),
            *["_" for _ in range(len(guessing_word))],
        )
