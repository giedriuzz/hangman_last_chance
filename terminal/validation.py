"""Module for validating inputs"""


def input_only_string(input_text: str) -> str:
    """Validate input is a input_text
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.replace(" ", "").isalpha() is True:
            return string
        else:
            print("Input must to be a string !")
