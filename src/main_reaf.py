"""Module for game logic"""
from database_main import DatabaseIntermediate
from inputs import input_email, input_passwd
from termcolor import colored
from validation import input_only_letters

db_base = DatabaseIntermediate("hangman")


# grąžina listą su: name, surname, email, passwd
def registration() -> None:
    """Function for user registration"""
    name = input_only_letters(colored("\nName: ", "white", attrs=["bold"]))
    surname = input_only_letters(colored("Surname: ", "white", attrs=["bold"]))
    email, passwd = input_email(), input_passwd()
    db_base.register_user(
        name=name, surname=surname, email=email, passwd=passwd
    )  # noqa:501


# if register == 1:
#     # grąžina listą su: name, surname, email, passwd
#     print(
#         f'\n{colored("             Register              ","black", "on_white", attrs=["bold"])}'  # noqa: E501
#     )
#     name = input_only_letters(colored("\nName: ", "white", attrs=["bold"]))  # noqa:E501
#     surname = input_only_letters(
#         colored("Surname: ", "white", attrs=["bold"])
#     )  # noqa:E501
#     email, passwd = input_email(), input_passwd()
#     db_base.get_user_for_register(
#         name=name, surname=surname, email=email, passwd=passwd
#     )
#     print(colored("You are registered. Now can login.", "green", attrs=["bold"]))
#     continue
# if register == 2:
#     print(
#         colored(
#             "              Login                ",
#             "black",
#             "on_white",
#             attrs=["bold"],
#         ),
#         "\n",
#     )
#     email, passwd = input_email(), input_passwd()
#     user = db_base.check_user_by_passwd_mail(user_passwd=passwd, user_email=email)
#     if user is False:
#         print(colored("User not found!", "red", attrs=["bold"]))
#         continue
#     name = user[0]
#     user_id = user[1]
#     print(
#         f'{colored(name, "yellow", attrs=["bold"])}'
#         f'{colored(" you are logged in!", "yellow", attrs=["bold"])}'
#     )
# if register == 3:
#     quest = 1
# else:
#     quest = 0
