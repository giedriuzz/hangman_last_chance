from word import Word

word = Word("Hello")

print(*word.empty_word_list)

length = 10
while 0 < length:
    length -= 1
    print(f"used letter: {word.not_guessed_letters_list}")
    letter = input("input one letter: ")
    if word.length_of_word() == 1:
        if word.is_letter_in_word(letter=letter) is True:
            print(*word.replace_guessed_letter(letter=letter))

            if word.is_word_guessed() is True:
                print("You guessed the word")
                print(f"guess: {10 - length}")
                break
            print(f"You have {length} guesses left")
        else:
            print("You dont guessed a letter")
            print(*word.empty_word_list)
            print(f"You have {length} guesses left")
    else:
        if word.is_guessed_word_equal(letter) is True:
            print("You guessed the word !!!")
        if word.is_word_guessed() is False:
            print("You hanged !!!")
