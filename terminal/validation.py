"""Module for validating inputs"""


def input_only_string(input_text: str) -> str:
    """Validate input is a input_text
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.replace(" ", "").isalpha() is True:
            return string
        print("Input must to be a string !")


def input_only_integer_value_not_bigger(value_size: int, input_text: str) -> str:
    """Validate input is integer not bigger than value size
    value_size: what value max size can be
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.isdigit() is True and int(string) <= value_size:
            return string
        print(f"Input must to be an integer value not bigger than: {value_size} !")
