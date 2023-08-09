"""Module for work with guessing word from database"""

from typing import List, Optional
from abc import ABC, abstractmethod


class Abstract(ABC):
    """class for work with get words from database"""

    @abstractmethod
    def length_of_word(self):
        """class for work with get words from database"""

    @abstractmethod
    def is_letter_in_word(self, letter):
        """Check if a letter is in word"""

    @abstractmethod
    def is_guessed_word_equal(self, word):
        """Check if a word is equal to a guess"""


class Word(Abstract):
    """class for work with get words from database"""

    not_guessed_letters_list: List[str] = []
    guessed_letters_list: List[str] = []

    def __init__(self, word: str):
        self.word: str = word.upper()
        self.empty_word_list = ["_" for _ in range(len(self.word))]

    def length_of_word(self) -> int:
        """Return the number of letters in the given word"""
        return len(self.word)

    def is_word_guessed(self) -> str:
        """Return guessed word for write to db"""
        alpha = "".join(self.empty_word_list)
        return alpha.isalpha()

    def is_letter_in_word(self, letter: str) -> Optional[bool]:
        """Check if a letter is in the word"""
        letter_upper = letter.upper()
        if letter_upper in self.word:
            self.guessed_letters_list.append(letter_upper)
            return True
        if letter_upper not in self.word:
            self.not_guessed_letters_list.append(letter_upper)
            return False
        return letter

    def is_guessed_word_equal(self, word) -> bool:
        """Check if a word is equal to a guess"""
        if word.upper() == self.word:
            return True
        return False

    def is_letter_in_not_guessed_list(self, letter: str) -> str:
        """Check is a letter is in not guessed letters list"""
        if self.not_guessed_letters_list.count(letter.upper()) >= 2:
            return False
        return True

    def is_letter_used(self, letter: str) -> bool:
        """Check is a letter is used"""
        letter_upper = letter.upper()
        if letter_upper in self.not_guessed_letters_list:
            return False
        if letter_upper in self.guessed_letters_list:
            return False
        return True

    def is_letter_in_guessed_list(self, letter: str) -> str:
        """Check is a letter is in guessed letters list"""
        if self.guessed_letters_list.count(letter.upper()) >= 2:
            return False
        return True

    def replace_guessed_letter(self, letter: str) -> list:
        """Replace a letter if it is in the word"""
        for get_letter in enumerate(self.word):
            if get_letter[1] == letter.upper():
                self.empty_word_list[get_letter[0]] = letter.upper()
            continue
        return self.empty_word_list


if __name__ == "__main__":
    pass
