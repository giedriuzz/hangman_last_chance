"""Module for store text where is used in program"""
from termcolor import colored
from validation import input_only_email
import maskpass


def login_register_text() -> str:
    """Text for registration"""
    text = (
        f"\n{colored('        1. Register', 'green', attrs=['bold'])}"
        f"\n{colored('        2. Login', 'yellow', attrs=['bold'])}"
        f"\n"
        f"\n{colored('Choose: ', 'blue')}"
    )
    return text


def level() -> str:
    """Text for level"""
    text = (
        f'\n{colored("           Level               ","green", "on_light_grey", attrs=["bold"])}'  # noqa: E501
        f"\n\n{colored('        1. Easy', 'green', attrs=['bold'])}"
        f"\n{colored('        2. Medium', 'yellow', attrs=['bold'])}"
        f"\n{colored('        3. Hard', 'red', attrs=['bold'])}"
        f"\n\n{colored('Choose: ', 'blue')}"
    )
    return text


def game_menu() -> str:
    """Text for game menu"""
    text = (
        f'\n{colored("           Game menu               ","green", "on_light_grey", attrs=["bold"])}'  # noqa: E501
        f'\n\n{colored("        1. Start the game", "yellow", attrs=["bold"])}'
        f'\n{colored("        2. Rules", "green", attrs=["bold"])}'
        f'\n{colored("        3. Quit", "red", attrs=["bold"])}'
        f'\n\n{colored("Choose: ", "blue")}'
    )
    return text


def input_email() -> str:
    """Text for input email"""
    email = input_only_email(colored("\nEmail: ", "yellow"))
    return email
    # return text


def input_passwd() -> str:
    """Text for input password"""
    passwd = maskpass.askpass(prompt=colored("Password: ", "yellow"), mask="*")
    return passwd
