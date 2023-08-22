"""Module for work with guessing word from database"""

from abc import ABC, abstractmethod
from typing import Union, List


class Abstract(ABC):
    """class for work with get words from database"""

    @abstractmethod
    def length_of_word(self) -> int:
        """class for work with get words from database"""

    @abstractmethod
    def lenght_of_unique_letters(self) -> bool:
        """Check if a word is equal to a guess"""

    @abstractmethod
    def is_word_guessed(self) -> bool:
        """Check if a letter is in word"""


class Word(Abstract):
    """class for work with get words from database"""

    def __init__(self, word: str):
        self.word = word.upper()
        self.empty_word_list = ["_" for _ in range(len(self.word))]

    def length_of_word(self) -> int:  # ! kol kas nenaudojama
        """Return the number of letters in the given word"""
        return len(self.word)

    def lenght_of_unique_letters(self) -> int:
        """Return the number of unique letters in the given word"""
        return len(set(self.word))

    def is_word_guessed(self) -> bool:
        """Return guessed word for write to db"""
        alpha = "".join(self.empty_word_list)
        if alpha.isalpha() is True:
            return True
        return False


class Letter(Word):
    """Class for work with letters"""

    LETTERS_LIST = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    MATCHED_LETTERS: List[str] = []
    NOT_MATCHED_LETTERS: List[str] = []

    def input_only_en_letters(self, input_text: str) -> str:
        """Validate input is it only letters from English alphabet
        and not use used letters before
        input_text: what text want to see in input line"""
        lt_letters_list = ["Ą", "Č", "Ę", "Ė", "Į", "Š", "Ų", "Ū", "Ž"]
        while True:
            string = input(input_text).upper()
            if string.isalpha() is True:
                if (
                    string not in self.MATCHED_LETTERS
                    and string not in self.NOT_MATCHED_LETTERS
                ):
                    filtered = filter(lambda letter: letter in string, lt_letters_list)
                    if len(list(filtered)) == 0:
                        return string
                print("You have already used this letter!")
                continue
            print("Input accepts only English alphabetic letters!")
            continue

    def is_letter_in_word(self, letter: str) -> Union[bool, str]:
        """Check if a letter is in the word"""
        if letter in self.word:
            self.MATCHED_LETTERS.append(letter)
            return True
        if letter not in self.word:
            self.NOT_MATCHED_LETTERS.append(letter)
            return False
        return letter

    def is_letter_in_not_guessed_list(
        self, letter: str
    ) -> bool:  # ! kol kas nenaudojama
        """Check is a letter is in not guessed letters list"""
        if self.NOT_MATCHED_LETTERS.count(letter.upper()) >= 2:
            return False
        return True

    def is_letter_used(self, letter) -> bool:
        """Check is a letter is used"""
        if letter.upper() in self.MATCHED_LETTERS:
            return False
        return True

    def is_letter_in_letters_list(self) -> bool:  # ! kol kas nenaudojama
        """Check is a letter in LETTERS_LIST"""
        if self.LETTERS_LIST is True:
            return True
        return False

    def replace_guessed_letter(self, letter) -> list:
        """Replace a letter if it is in the word"""
        for get_letter in enumerate(self.word):
            if get_letter[1] == letter.upper():
                self.MATCHED_LETTERS.append(get_letter[1].upper())
                self.empty_word_list[get_letter[0]] = letter.upper()
            continue
        return self.empty_word_list

    def remove_used_letter_from_list(self, letter) -> List[str]:
        """Remove used letter from list"""
        self.LETTERS_LIST.remove(letter.upper())
        return self.LETTERS_LIST

    def get_hangman(self, letter: str) -> int:
        """Return hangman picture"""
        return self.NOT_MATCHED_LETTERS.index(letter.upper())


if __name__ == "__main__":
    pass
