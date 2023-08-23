"""Main game script"""

import sys
from random import choice

from hangman import hangman
from main import Letter, Word
from rules import rules
from termcolor import colored
from validation import input_only_integer_value_not_bigger
from words.words import words

greeting = colored(
    " === Welcome to Hangman game! ===", "red", "on_light_blue", attrs=["bold"]
)
print("\n", greeting, "\n")


while True:
    CHOOSING = int(
        input_only_integer_value_not_bigger(
            3,
            f'\n{colored("1. Start the game", "yellow", attrs=["bold"])}'
            f'\n{colored("2. Rules", "green", attrs=["bold"])}'
            f'\n{colored("3. Quit", "red", attrs=["bold"])}'
            f'\n{colored("Choose: ", "blue")}',
        )
    )
    if CHOOSING == 1:
        # * Game area
        categories = {1: "Countries", 2: "Animals", 3: "Fruits"}
        category = int(
            input_only_integer_value_not_bigger(
                3,
                f'\n{colored("1. Countries", "yellow", attrs=["bold"])}'
                f'\n{colored("2. Animals", "green", attrs=["bold"])}'
                f'\n{colored("3. Fruits", "red", attrs=["bold"])}'
                f'\n{colored("Choose: ", "blue")}',
            )
        )
        get_category_value = categories[category]

        _SAY_DONT_GUESSED = "You don`t guessed a letter :("
        _say_guessing_word = colored("Guessing word: ", "blue", attrs=["bold"])
        _say_you_hanged = f'\n{colored("HANGED :( ", "red", "on_red", attrs=["bold"])}'
        _say_choose_category = colored("Category: ", "green")

        def get_category_word(category_chooses: int) -> str:
            """Get random word from category"""
            return choice(words[category_chooses])

        LENGTH_ONE = 0
        while LENGTH_ONE < 10:
            LENGTH_ONE += 1

            guessed_word = get_category_word(category)
            guessed_word_in_list = list(guessed_word)
            word = Word(guessed_word)
            letter = Letter(guessed_word)
            letter.MATCHED_LETTERS.clear()
            letter.NOT_MATCHED_LETTERS.clear()

            print(f'\n{colored("Round: ", "red")} {LENGTH_ONE}/10')
            print(_say_choose_category, get_category_value)
            print(_say_guessing_word, *word.empty_word_list)

            while True:
                string = letter.input_only_en_letters(
                    colored("Guess a letter or all word: ", "yellow")
                )
                if len(string) == 1:
                    # * When letter is in word
                    if letter.is_letter_in_word(string) is True:
                        print(_say_choose_category, get_category_value)
                        print(
                            colored("Guessing word: ", "blue"),
                            *letter.replace_guessed_letter(string),
                        )
                        if letter.is_word_guessed() is True:
                            print(colored(" == You guessed the word !!! == ", "yellow"))
                            break
                        print(
                            colored("Letters left: ", "green"),
                            *letter.remove_used_letter_from_list(string),
                        )
                        continue
                    # * When letter is not in word
                    if letter.get_hangman(string) == 7:
                        print(_say_you_hanged)
                        print(colored(hangman[letter.get_hangman(string)], "red"))
                        print(
                            colored("Word was: ", "blue", attrs=["bold"]),
                            *guessed_word_in_list,
                        )

                        break
                    print(colored(_SAY_DONT_GUESSED, "red"))
                    print(hangman[letter.get_hangman(string)])
                    print(_say_choose_category, get_category_value)
                    print(
                        colored("Guessing word: ", "blue"),
                        *letter.replace_guessed_letter(string),
                    )
                    print(
                        colored("Letters left: ", "green"),
                        *letter.remove_used_letter_from_list(string),
                    )
                    continue
                # * When word is not guessed
                if letter.is_word_equal(string) is False:
                    print(_say_you_hanged)
                    print(colored(hangman[7], "red"))
                    print(
                        colored("Word was: ", "blue", attrs=["bold"]),
                        *guessed_word_in_list,
                    )

                    break
                print(colored(" == You guessed the word !!! == ", "yellow"))
                break
        print(colored(" == Game over == ", "red"))

    elif CHOOSING == 2:
        rules()

    elif CHOOSING == 3:
        print(
            f'{colored("Closed game application!", "red")}\n'
            f'If you want to play again, run {colored("app.py", "red",attrs=["bold"])} file!'
        )

        sys.exit(0)
