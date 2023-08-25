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

First clone a repository, it will be better if you create you own python environment.

```
git clone https://github.com/giedriuzz/Hangman_last_chance.git
```
Import all libs from `requirements.txt` or from `Pipfile.lock`  
And run `app.py` file where is in **`terminal`** folder.

```
python app.py
```

If you don`t have virtual environment just run

```
python3 app.py
```

## Add new Categories and Words

To edit or add new `Categories` and `words` you must edit `words.py` file where is in **`words`** folder.  

#### `words.py`

```python
words = {
    "Countries: [
        "AFGHANISTAN",
        "ALBANIA",
        "ALGERIA",
    ],
    "NEW_CATEGORY": [  
        "New_word_1",  
        "New_word_2
    ]
```


***

Game running in two **[Docker](https://www.docker.com)** containers. One container hold database an in other one Hangman application.  
