"""Main game script"""

import logging
import logging.config
import sys
import datetime
from random import choice

from database_main import DatabaseIntermediate
from hangman import hangman
from main import Categories, Letter, Words
from rules import rules
from termcolor import colored
from validation import (
    get_unique_id,
    input_only_en_letters,
    input_only_integer_value_not_bigger,
    input_only_letters,
    return_dict_value_by_key,
    get_gaming_time,
)
from inputs import login_register_text, input_email, input_passwd, game_menu, level


def game(db_name: str) -> None:
    """Class for all game data"""

    db_base = DatabaseIntermediate(db_name=db_name)

    logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False)
    logger = logging.getLogger("sampleLogger")

    greeting = colored(
        " === Welcome to Hangman game! === ", "black", "on_white", attrs=["bold"]
    )
    print("\n", greeting)

    while True:
        register = input_only_integer_value_not_bigger(3, login_register_text())
        if register == 1:
            print(
                colored(
                    "            Register               ",
                    "green",
                    "on_light_grey",
                    attrs=["bold"],
                )
            )
            name = input_only_letters(colored("\nName: ", "yellow"))
            surname = input_only_letters(colored("Surname: ", "yellow"))
            email, passwd = input_email(), input_passwd()
            db_base.get_user_for_register(
                name=name, surname=surname, email=email, passwd=passwd
            )
            print(
                colored("You are registered. Now can login.", "green", attrs=["bold"])
            )
            continue

        if register == 2:
            print(
                colored(
                    "              Login                ",
                    "green",
                    "on_light_grey",
                    attrs=["bold"],
                )
            )
            email, passwd = input_email(), input_passwd()
            user = db_base.check_user_by_passwd_mail(
                user_passwd=passwd, user_email=email
            )
            if user is False:
                print(colored("User not found!", "red", attrs=["bold"]))
                continue
            name = user[0]
            user_id = user[1]
            print(
                f'{colored(name, "yellow", attrs=["bold"])}'
                f'{colored(" you are logged in!", "yellow", attrs=["bold"])}'
            )
        while True:
            choosing = int(input_only_integer_value_not_bigger(3, game_menu()))
            print()
            # * Game area
            if choosing == 1:
                _say_you_hanged = (
                    f'\n{colored("HANGED :( ", "red", "on_red", attrs=["bold"])}'
                )
                _say_choose_category = colored("Category: ", "green")
                _say_guessed_word = colored(
                    " == You guessed the word !!! == ", "yellow"
                )
                categories = Categories(db_base.get_category())
                categories_dict = categories.get_categories_enumerated()
                category = return_dict_value_by_key(
                    len(categories_dict),
                    categories.print_categories(categories_dict),
                    categories_dict,
                )
                difficulty = input_only_integer_value_not_bigger(3, level())
                words_dict = db_base.get_words_by_category_difficulty(
                    category=category, difficulty=difficulty
                )
                length = 0
                game_id = get_unique_id()
                while length < 10:
                    length += 1
                    start_time = datetime.datetime.now()

                    logging.debug("Round: %s/10", length)  # * Logging
                    logger.debug("Category: %s", category)  # * Logging
                    guessing_word = choice(words_dict)
                    logger.debug("Guessing word: %s", guessing_word)  # * Logging
                    guessed_word_in_list = list(guessing_word)
                    word_declaration = Words(word=guessing_word)

                    letter = Letter(word_declaration, "")
                    letter.LETTERS_LIST.clear()
                    letter.reload_letters_list()
                    letter.MATCHED_LETTERS.clear()
                    letter.NOT_MATCHED_LETTERS.clear()
                    letter.empty_word_list.clear()

                    print(f'\n{colored("Round: ", "red")} {length}/10')
                    print(_say_choose_category, category)
                    print(
                        colored("Letters left: ", "green"), *letter.LETTERS_LIST_TUPLE
                    )
                    print(
                        colored("Guessing word: ", "blue", attrs=["bold"]),
                        *["_" for _ in range(len(guessing_word))],
                    )
                    while True:
                        string_only_en_letters = input_only_en_letters(
                            colored("Guess a letter or all word: ", "yellow")
                        )
                        logger.debug(
                            "Letter in input() : %s", string_only_en_letters
                        )  # * Logging
                        letter = Letter(word_declaration, string_only_en_letters)
                        letter.create_empty_word_list()
                        if letter.inspect_letters() is False:
                            continue
                        string = letter.inspect_letters()
                        if len(string_only_en_letters) == 1:
                            # * When letter is in word
                            if letter.is_letter_in_word() is True and string is True:
                                print(_say_choose_category, category)
                                print(
                                    colored("Guessing word: ", "blue"),
                                    *letter.replace_guessed_letter(),
                                )
                                if letter.is_word_guessed() is True:
                                    hanged_bool = True
                                    print(_say_guessed_word)
                                    logger.debug(
                                        "Guessed word: %s", guessing_word
                                    )  # * Logging
                                    logger.debug("Win a GAME!")  # * Logging

                                    break
                                print(
                                    colored("Letters left: ", "green"),
                                    *letter.remove_used_letter_from_list(),
                                )
                                logger.debug(
                                    "Guessed letter: %s", string_only_en_letters
                                )  # * Logging
                                continue
                            # * When letter is not in word
                            if letter.get_hangman() == 7:
                                hanged_bool = False
                                print(_say_you_hanged)
                                print(colored(hangman[letter.get_hangman()], "red"))
                                print(
                                    colored("Word was: ", "blue", attrs=["bold"]),
                                    *guessed_word_in_list,
                                )
                                logger.debug("Lose a GAME!")  # * Logging
                                break
                            print(colored("You don`t guessed a letter :(", "red"))
                            print(hangman[letter.get_hangman()])
                            print(_say_choose_category, category)
                            print(
                                colored("Guessing word: ", "blue"),
                                *letter.replace_guessed_letter(),
                            )
                            print(
                                colored("Letters left: ", "green"),
                                *letter.remove_used_letter_from_list(),
                            )
                            logger.debug(
                                "Not guessed letter was: %s", string_only_en_letters
                            )  # * Logging
                            continue
                        # * When word is in input
                        if letter.is_word_equal(string_only_en_letters) is False:
                            hanged_bool = False
                            print(_say_you_hanged)
                            print(colored(hangman[7], "red"))
                            print(
                                colored("Word was: ", "blue", attrs=["bold"]),
                                *guessed_word_in_list,
                            )
                            logger.debug(
                                "Not guesses word in input(): %s",
                                string_only_en_letters,
                            )  # * Logging
                            logger.debug("Lose a ROUND!")  # * Logging
                            break
                        hanged_bool = True
                        logger.debug("Win a GAME!")  # * Logging
                        print(_say_guessed_word)
                        break

                    finish_time = datetime.datetime.now()
                    guess_time = get_gaming_time(finish_time, start_time)

                    db_base.add_round(
                        game_id=game_id,
                        word=guessing_word,
                        guess_time=guess_time,
                        hanged=hanged_bool,
                        guesses_made=letter.get_guesses(),
                        user_id=user_id,
                    )
                db_base.get_game_info(game_id=game_id)
                db_base.get_rounds_info(game_id=game_id)
                logger.debug("GAME OVER!")  # * Logging
                print(
                    colored(
                        "          == GAME OVER ==          ",
                        "white",
                        "on_red",
                        attrs=["bold"],
                    )
                )
            # * Rules area
            elif choosing == 2:
                rules()
            # * Quit area
            elif choosing == 3:
                print(
                    f'{colored("Closed game application!", "red")}\n'
                    f"If you want to play again, run "
                    f'{colored("app_db.py", "red",attrs=["bold"])} file!'
                )

                sys.exit(0)


game(db_name="hangman")
