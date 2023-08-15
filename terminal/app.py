"""Main game script"""
import time
import sys
from termcolor import colored, cprint
from word import Word
from validation import input_only_string, input_only_integer_value_not_bigger
from hangman import hangman

word = Word("Hello")

greeting = colored(
    " === Welcome to Hangman game! ===", "white", "on_light_blue", attrs=["bold"]
)
print("\n", greeting, "\n")

CHOOSING = int(
    input_only_integer_value_not_bigger(
        3, "1. Start the game\n2. Rules\n3. Quit\nChoose: "
    )
)

if CHOOSING == 1:
    # Game area
    EMPTY_WORD = word.empty_word_list
    _SAY_DONT_GUESSED = "You don`t guessed a letter :("
    _SAY_GUESSED_LETTER = "You guessed a letter ! "
    print("Guess the word: ", *EMPTY_WORD)

    LENGTH = 10
    while 0 < LENGTH:
        LENGTH -= 1
        not_guessed_letters = word.not_guessed_letters_list
        letter = input_only_string(colored("Guess a letter or all word: ", "yellow"))
        hanged = colored(hangman[7], "red")
        if word.is_letter_used(letter) is True:
            if len(letter) == 1:
                if word.is_letter_in_word(letter=letter) is True:
                    guessing_word = word.replace_guessed_letter(letter=letter)
                    JOINED_GUESSING_WORD = "".join(guessing_word)
                    if JOINED_GUESSING_WORD.isalpha() is True:
                        print(
                            f" = You guessed the word !!! -> {colored(JOINED_GUESSING_WORD,'yellow', attrs=['blink'] )}"
                        )
                        break
                    print(colored(_SAY_GUESSED_LETTER, "green"))
                    print(*guessing_word)
                    print(f"You have {LENGTH} guesses left")
                else:
                    letter_index = not_guessed_letters.index(letter.upper())
                    if letter_index <= 7:
                        print(colored(_SAY_DONT_GUESSED, "light_red"))
                        print(f"You have {colored(LENGTH, 'red')} guesses left.")
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
elif CHOOSING == 2:
    print("Rules area")


elif CHOOSING == 3:
    print("Quit area")
    sys.exit(0)
