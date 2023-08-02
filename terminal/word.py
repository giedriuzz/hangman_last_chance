from typing import List


class Word:
    guessed_letters_list: List[str] = []
    # guess_word_list: List[str] = []
    # empty_word_list: List[str] = []

    def __init__(self, word: str):
        self.word = word
        self.guess_word_list = [letter for letter in self.word]
        self.empty_word_list = ["_" for _ in range(len(self.word))]

    # def create_guess_word_lists(self) -> List[str]:
    #     self.guess_word_list = [letter for letter in self.word]
    #     self.empty_word_list = [self.empty_word_list.append('_') for _ in range(len(self.word))]
    #     return self.guess_word_list

    def is_letter_in_word(self, letter):
        self.letter = letter
        if letter in self.word:
            return True
        else:
            return False

    def replace_guessed_letter(self):
        for get_letter in enumerate(self.word):
            if get_letter[1] == self.letter:
                self.guessed_letters_list.append(self.letter)
                self.empty_word_list[get_letter[0]] = self.letter
            continue
        return self.empty_word_list

    def is_word_guessed(self):
        alpha = "".join(self.empty_word_list)
        return alpha.isalpha()


if __name__ == "__main__":
    word = Word("Hello")
    print(word.guess_word_list)
    print(word.empty_word_list)

    length = 10
    while 0 < length:
        length -= 1
        letter = input("input one letter: ")
        if word.is_letter_in_word(letter) is True:
            print(word.replace_guessed_letter())
            print(word.count_guessed_letters())
            print(f"You have {length} guesses left")
            # print(word.empty_word_list)
            # letter = input("input one letter: ")
        else:
            print("You dont guessed a letter")
            print(word.empty_word_list)
            print(f"You have {length} guesses left")
