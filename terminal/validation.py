"""Module for validating inputs"""


# * perkelta į word.py
def input_only_en_letters(input_text: str) -> str:
    """Validate input is it only letters from English alphabet
    input_text: what text want to see in input line"""
    lt_letters_list = ["Ą", "Č", "Ę", "Ė", "Į", "Š", "Ų", "Ū", "Ž"]
    while True:
        string = input(input_text).upper()
        if string.isalpha() is True:
            filtered = filter(lambda letter: letter in string, lt_letters_list)
            if len(list(filtered)) == 0:
                return string
        print("Input accepts only English alphabetic letters!")
        continue


def input_only_integer_value_not_bigger(value_size: int, input_text: str) -> str:
    """Validate input is integer not bigger than value size
    value_size: what value max size can be
    input_text: what text want to see in input line"""
    while True:
        string = input(input_text)
        if string.isdigit() is True and int(string) <= value_size:
            return string
        print(f"Input must to be an integer value not bigger than: {value_size} !")
