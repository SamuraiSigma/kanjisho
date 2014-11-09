"""User-dictionary interaction functions are here"""

import random
import sys
import subprocess
import romkan
from kanji import Kanji

OP_CHAR = '#'  # Char used for dictionary special options.


def search(jisho):
    """Dictionary mode, where kanji previously read can be searched"""
    while True:
        x = input("Type in something to search for it: ")

        if x == OP_CHAR:
            options()

        elif x == OP_CHAR + "exit":
            break

        elif x == OP_CHAR + "all":
            clear_screen()
            i = 0
            for kanji in jisho:
                jisho[kanji]()
                i += 1
                if i % 6 == 0:
                    input()
                    clear_screen()
            input()
            clear_screen()

        elif x == OP_CHAR + "clear":
            clear_screen()

        elif x == OP_CHAR + "game":
            game(jisho)

        elif x in jisho:
            jisho[x]()

        else:
            hiragana = romkan.to_hiragana(x)
            katakana = romkan.to_katakana(x)
            for kanji in jisho:
                if x in jisho[kanji].meaning:
                    print(kanji, "=", x)
                elif hiragana in jisho[kanji].kunyomi:
                    print(kanji, "->", hiragana)
                elif katakana in jisho[kanji].onyomi:
                    print(kanji, "~>", katakana)


def options():
    """Shows all extra options available in the dictionary"""
    print("Use '" + OP_CHAR + "' before each of these commands:\n")
    print("- all: Shows all kanji inside the dictionary.")
    print("- clear: Clears screen.")
    print("- exit: Exits program.")
    print("- game: Plays the kanji game!")
    print()


def clear_screen():
    """Uses the 'clear' option from the OS"""
    if sys.platform == "linux":
        subprocess.call("clear")
    elif sys.platform == "win32":
        subprocess.call("cls", shell=True)


def game(jisho):
    """Plays the random kanji game!"""
    while True:
        rounds = int(input("How many rounds do you want to play? "))   
        if rounds > 0:
            break

    correct = 0
    count = rounds
    while count > 0:
        count -= 1
        kanji = random.choice(list(jisho.keys()))
        quiz = random.randint(0, 2)

        if quiz == 0:
            answer = input("What does " + kanji + " mean? ")
            if answer in jisho[kanji].meaning:
                print("Correct! :D")
                correct += 1
            else:
                print("Incorrect!", kanji, "=", jisho[kanji].meaning)

        if quiz == 1:
            answer = input("Type in one of the kunyomi of " + kanji + " : ")
            if romkan.to_hiragana(answer) in jisho[kanji].kunyomi:
                print("Correct! :D")
                correct += 1
            else:
                print("Incorrect!")
            print(kanji, "=", jisho[kanji].kunyomi)

        if quiz == 2:
            answer = input("Type in one of the onyomi of " + kanji + " : ")
            if romkan.to_katakana(answer) in jisho[kanji].onyomi:
                print("Correct! :D")
                correct += 1
            else:
                print("Incorrect!")
            print(kanji, "=", jisho[kanji].onyomi)

    print(">> You got " + str(correct) + " out of " + str(rounds) + " (" + str(100*correct/rounds) + "%)!\n")
