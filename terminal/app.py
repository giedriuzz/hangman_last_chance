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
            # stop = word.lenght_of_unique_letters()

            while True:
                string = letter.input_only_en_letters(
                    colored("Guess a letter or all word: ", "yellow")
                )

                if len(string) == 1:
                    # * Kai atspėta raidė
                    if (
                        letter.is_letter_in_word(string) is True
                    ):  # TODO: refaktorinti per daug ifu
                        # print(guesses_left)
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
                    # print(guesses_left)
                    print(
                        colored("Guessing word: ", "blue"),
                        *letter.replace_guessed_letter(string),
                    )
                    print(
                        colored("Letters left: ", "green"),
                        *letter.remove_used_letter_from_list(string),
                    )
            print(_say_you_hanged)  # Kai neatspėtas žodis
            # [ ] atspausdinti hangman
            # [ ] atspausdinti kiek liko raidžių
            # [ ] atspausdinti žodį

            # print("Letters left: ", *letter.remove_used_letter_from_list())
            # print(replace_letter)
            # break

    #     if word.is_letter_used(letter) is True:
    #         if word.is_letter_in_word(letter=letter) is True:
    #             guessing_word = word.replace_guessed_letter(letter=letter)
    #             JOINED_GUESSING_WORD = "".join(guessing_word)
    #             if JOINED_GUESSING_WORD.isalpha() is True:
    #                 print(
    #                     f" = You guessed the word !!! -> {colored(JOINED_GUESSING_WORD,'yellow', attrs=['blink'] )}"
    #                 )
    #                 break
    #             print(colored(_SAY_GUESSED_LETTER, "green"))
    #             print(*guessing_word)
    #             print(f"You have {LENGTH} guesses left")
    #         else:
    #             letter_index = not_guessed_letters.index(letter.upper())  # [ ]
    #             if letter_index <= 6:
    #                 print(colored(_SAY_DONT_GUESSED, "light_red"))
    #                 print(f"You have {colored(LENGTH, 'red')} guesses left.")
    #                 print(hangman[letter_index])
    #             else:
    #                 print(hanged)
    #                 break
    #     else:
    #         if word.is_guessed_word_equal(letter) is True:
    #             print("You guessed the word !!!")
    #             break
    #         if word.is_guessed_word_equal(letter) is False:
    #             print(hanged)
    #             print("You hanged !!!")
    #             break
    # else:
    #     print(f"You used '{letter}' letter  before!")
    #     print(f"You have {LENGTH} guesses left")

    # print("Used letter: ", *not_guessed_letters)


# elif CHOOSING == 2:
#     print("Rules area")


# elif CHOOSING == 3:
#     print("Quit area")
#     sys.exit(0)

print(main())
