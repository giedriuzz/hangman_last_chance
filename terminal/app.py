"""Main game script"""

import sys
from termcolor import colored
from word import Word, Letter
from validation import input_only_integer_value_not_bigger
from hangman import hangman


greeting = colored(
    " === Welcome to Hangman game! ===", "red", "on_light_blue", attrs=["bold"]
)
print("\n", greeting, "\n")

CHOOSING = int(
    input_only_integer_value_not_bigger(
        3, "1. Start the game\n2. Rules\n3. Quit\nChoose: "
    )
)


def main():
    if CHOOSING == 1:
        # * Game area
        _say_guessing_word = colored("Guessing word: ", "blue", attrs=["bold"])
        _say_dont_guessed = "You don`t guessed a letter :("
        _say_you_hanged = colored(" You HANGED :( ", "red", "on_red", attrs=["bold"])

        length_one = 0
        while length_one < 10:  # * Can play 10 rounds
            length_one += 1
            guessed_word = "Hello"  # TODO: Pasidaryti kad gautų iš DB
            word = Word(guessed_word)
            letter = Letter(guessed_word)

            print(f'\n{colored("Round: ", "red")} {length_one}/10')
            print(_say_guessing_word, *word.empty_word_list)

            while True:
                string = letter.input_only_en_letters(
                    colored("Guess a letter or all word: ", "yellow")
                )
                if len(string) == 1:
                    # * Kai atspėta raidė
                    if letter.is_letter_in_word(string) is True:
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
                    # * Kai neatspėta raidė
                    if letter.get_hangman(string) == 7:
                        print(_say_you_hanged)
                        print(colored(hangman[letter.get_hangman(string)], "red"))
                        break
                    print(colored(_say_dont_guessed, "red"))
                    print(hangman[letter.get_hangman(string)])
                    print(
                        colored("Guessing word: ", "blue"),
                        *letter.replace_guessed_letter(string),
                    )
                    print(
                        colored("Letters left: ", "green"),
                        *letter.remove_used_letter_from_list(string),
                    )
                    continue
                if letter.is_word_equal(string) is False:
                    print(colored(hangman[7], "red"))
                    print(_say_you_hanged)
                    break
                print(colored(" == You guessed the word !!! == ", "yellow"))
                break
        print(colored(" == Game over == ", "red"))


# elif CHOOSING == 2:
#     print("Rules area")


# elif CHOOSING == 3:
#     print("Quit area")
#     sys.exit(0)

print(main())
