"""Module for validating inputs"""
from termcolor import colored


def input_only_en_letters(input_text: str) -> str:
    """Validate input is a input_text
    input_text: what text want to see in input line"""

    lt_letters_list = ["Ą", "Č", "Ę", "Ė", "Į", "Š", "Ų", "Ū", "Ž"]
    while True:
        string = input(input_text).upper()
        if len(string) == 1:
            if (
                string not in lt_letters_list
                and string.replace(" ", "").isalpha() is True
            ):
                return string
            print("Input must to be a string or only English alphabet letter !")
        else:
            for _ in range(len(string)):
                for letter in string:
                    if letter in lt_letters_list:
                        print(
                            f'Letter {colored(letter, "red")} in word must to be from English alphabetic letter'
                        )
                    continue
                return string
        # Word.not_guessed_letters_list.append(string) # FIXME #? ar reikia tos eilutės


def input_only_integer_value_not_bigger(value_size: int, input_text: str) -> str:
    """Validate input is integer not bigger than value size
    value_size: what value max size can be
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.isdigit() is True and int(string) <= value_size:
            return string
        print(f"Input must to be an integer value not bigger than: {value_size} !")
