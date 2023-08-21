"""Main game script"""

import sys
from termcolor import colored
from word import Word, Letter
from validation import input_only_en_letters, input_only_integer_value_not_bigger
from hangman import hangman


greeting = colored(
    " === Welcome to Hangman game! ===", "white", "on_light_blue", attrs=["bold"]
)
print("\n", greeting, "\n")

CHOOSING = int(
    input_only_integer_value_not_bigger(
        3, "1. Start the game\n2. Rules\n3. Quit\nChoose: "
    )
)


def main():
    if CHOOSING == 1:
        # Game area
        guessed_word = "Hello"  # Padaryti kad gautų iš DB
        word = Word(guessed_word)
        _SAY_DONT_GUESSED = "You don`t guessed a letter :("
        _SAY_GUESSED_LETTER = "You guessed a letter ! "
        length = 0
        while length < 10:
            length += 1
            print(f'\n{colored("Round: ", "red")} {length}/10')
            print("Guess the word: ", *word.empty_word_list)
            lenght_two = 0
            while lenght_two < 10:
                lenght_two += 1
                string = input_only_en_letters(
                    colored("Guess a letter or all word: ", "yellow")
                )
                letter = Letter(
                    string
                )  # FIXME #! Ar reikia čia tos eilutės DUBLIUOJASI

                if len(string) == 1:
                    if letter.is_letter_in_word() is True:
                        print(letter.replace_guessed_letter())
                        continue

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
