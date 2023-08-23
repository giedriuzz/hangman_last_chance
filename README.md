# 'Hangman' last chance

This is last work the end of learning programming language of python in [CodeAcademy](https://codeacademy.lt/programavimo-kursai/python-pradedantiesiems-uzimtiems-asmenims/) school.

***

## Introduction

### Rules

How to play hangman :dart:  
Hangman is a simple word guessing game. Player try to figure out an unknown  
word by guessing letters. If too many letters which do not appear in the word  
are guessed, the player is hanged (and loses).
<p align="center" width="100%">
<img width="15%" src="terminal/pictures/hanged.png">
</p>

As letters in the word are guessed, choose and write letter in terminal.  
If a letter not in the word is guess, you will see picture of a person on the  
gallows–one part for each incorrect letter guess. Most frequently, the person  
is drawn in 7 parts (for 7 letter guesses) in the order: gallows, head, body,  
left leg, right leg, left arm, right arm, rope.

***

## Start a game

First clone a repository:

```
git clone https://github.com/giedriuzz/Hangman_last_chance.git
```
And run `app.py` file where is in **`terminal`** folder.

```
python app.py
```

If you don`t have virtual environment just run

```
python3 app.py
```

## Add new Words

To add new `Words` you must to edit `words.py` file where is in **`words`** folder.  
And just edit you choose category.

## Add new Categories

To add new `Categories` you must to edit `words.py` file where is in **`words`** folder.  

```python
words = {
    1: [
        "AFGHANISTAN",
        "ALBANIA",
        "ALGERIA",
    ]....
    4: ["New_word_1", 
        "New_word_2
    ]
```
And add new `Category` name in file `app.py`, need change `categories` and `category` variables.  

#### `category = `

```python
# category, add new category here
category = int(
            input_only_integer_value_not_bigger(
                3,
                f'\n{colored("1. Countries", "yellow", attrs=["bold"])}'
                f'\n{colored("2. Animals", "green", attrs=["bold"])}'
                f'\n{colored("3. Fruits", "red", attrs=["bold"])}'
                f'\n{colored("4. [ NEW_CATEGORY ]", "red", attrs=["bold"])}' # example
                f'\n{colored("Choose: ", "blue")}',
            )
        )
```

#### `categories = `

```python
# categories, add new category here
categories = {1: "Countries", 2: "Animals", 3: "Fruits", 4: [ NEW_CATEGORY ]}
```

***

Game running in two **[Docker](https://www.docker.com)** containers. One container hold database an in other one Hangman application.  
