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

    def __init__(self, word: str):
        self.word: str = word.upper()
        self.empty_word_list = ["_" for _ in range(len(self.word))]

    def length_of_word(self) -> int:
        """Return the number of letters in the given word"""
        return len(self.word)

    def is_letter_in_word(self, letter: str) -> Optional[bool]:
        """Check if a letter is in the word"""
        if letter.upper() in self.word:
            return True
        if letter.upper() not in self.word:
            self.not_guessed_letters_list.append(letter.upper())
            return False
        return letter

    def is_guessed_word_equal(self, word) -> bool:
        """Check if a word is equal to a guess"""
        if word.upper() == self.word:
            return True
        return False

    def replace_guessed_letter(self, letter: str) -> list:
        """Replace a letter if it is in the word"""
        for get_letter in enumerate(self.word):
            if get_letter[1] == letter.upper():
                self.empty_word_list[get_letter[0]] = letter.upper()
            continue
        return self.empty_word_list

    def is_word_guessed(self) -> str:
        """Return guessed word for write to db"""
        alpha = "".join(self.empty_word_list)
        return alpha.isalpha()


if __name__ == "__main__":
    pass
