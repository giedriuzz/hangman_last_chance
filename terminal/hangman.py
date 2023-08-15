"""Hangman pictures for visualization"""

import time
from termcolor import colored

hangman = [
    """
 +-----+
       |
       |
       |
       |
       |
      ===""",
    """
 +-----+
       |
 O     |
       |
       |
       |
      ===""",
    """
 +-----+
       |
 O     |
 |     |
       |
       |
      ===""",
    """
 +-----+
       |
 O     |
/|     |
       |
       |
      ===""",
    """
 +-----+
       |
 O     |
/|\    |
       |
       |
      ===""",
    """
 +-----+
       |
 O     |
/|\    |
/      |
       |
      ===""",
    """
 +-----+
       |
 O     |
/|\    |
/ \    |
       |
      ===""",
    """
 +-----+
 |     |
 O     |
/|\    |
/ \    |
       |
      ===""",
]

if __name__ == "__main__":
    print(hangman[0])
    for i in hangman:
        print(colored(i, "red", attrs=["blink"]))
        time.sleep(1)