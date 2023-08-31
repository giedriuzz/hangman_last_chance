"""Module for game logic"""

from database.db_intermediate import DatabaseIntermediate
from inputs import input_email, input_passwd
from main import Categories, Letter
from termcolor import colored
from validation import input_only_letters, return_dict_value_by_key

db_base = DatabaseIntermediate("hangman")


class Game:
    """Class for game methods"""

    def __init__(self, db_name) -> None:
        self.db_intermediate = DatabaseIntermediate(db_name)

    def registration(self) -> None:
        """Function for user registration"""
        print(
            f'\n{colored("             Register              ","black", "on_white", attrs=["bold"])}'  # noqa: E501
        )

        name = input_only_letters(colored("\nName: ", "white", attrs=["bold"]))
        surname = input_only_letters(colored("Surname: ", "white", attrs=["bold"]))
        email, passwd = input_email(), input_passwd()
        if self.db_intermediate.read_user_by_mail(user_email=email) is False:
            self.db_intermediate.register_user(
                name=name, surname=surname, email=email, passwd=passwd
            )
            print(
                colored("You are registered. Now can login.", "green", attrs=["bold"])
            )
        else:
            print(
                f'{colored("User with this email ","red", attrs=["bold"])}{email}{colored(" already exists!", "red", attrs=["bold"])}'
            )

    def login(self) -> None:
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
        name = user[0]
        user_id = user[1]
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
