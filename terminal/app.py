"""Main game script"""
import time
from termcolor import colored, cprint
from word import Word
from validation import input_only_string
from hangman import hangman

word = Word("Hello")

greeting = colored(
    " === Welcome to Hangman game! ===", "white", "on_light_blue", attrs=["bold"]
)
print("\n", greeting, "\n")
EMPTY_WORD = word.empty_word_list
print("Guess the word: ", *EMPTY_WORD)

LENGTH = 10
while 0 < LENGTH:
    LENGTH -= 1
    not_guessed_letters = word.not_guessed_letters_list
    letter = input_only_string(colored("Guess a letter or all word: ", "yellow"))
    hanged = colored(hangman[7], "red", "on_light_blue", attrs=["blink"])
    if word.is_letter_used(letter) is True:
        if len(letter) == 1:
            if word.is_letter_in_word(letter=letter) is True:
                guessing_word = word.replace_guessed_letter(letter=letter)
                joined_guessing_word = "".join(guessing_word)
                if joined_guessing_word.isalpha() is True:
                    print(
                        f" = You guessed the word !!! -> {colored(joined_guessing_word,'yellow', attrs=['blink'] )}"
                    )

                    break

                print(*guessing_word)
                print(f"You have {LENGTH} guesses left")
            else:
                letter_index = not_guessed_letters.index(letter.upper())
                if letter_index <= 7:
                    print("You dont guessed a letter")
                    print(f"You have {LENGTH} guesses left")
                    print(hangman[letter_index])
                else:
                    print(hanged)
                    break
        else:
            if word.is_guessed_word_equal(letter) is True:
                print("You guessed the word !!!")
                break
            if word.is_guessed_word_equal(letter) is False:
                print(hanged)
                print("You hanged !!!")
                break
    else:
        print(f"You used '{letter}' letter  before!")
        print(f"You have {LENGTH} guesses left")

    print("Used letter: ", *not_guessed_letters)
