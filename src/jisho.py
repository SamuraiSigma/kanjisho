"""User-dictionary interaction functions are here"""

import random
import sys
import subprocess
import romkan
from kanji import Kanji


def search(jisho, all_mode, rounds, verbose):
    """Dictionary mode, where kanji previously read can be searched"""
    if all_mode:
        show_all(jisho)
    elif rounds > 0:
        game(jisho, rounds)
    else:
        for x in sys.argv[1:]:
            if x in jisho:
                jisho[x]()
            else:
                hiragana = romkan.to_hiragana(x)
                katakana = romkan.to_katakana(x)
                for kanji in jisho:
                    if x in jisho[kanji].meaning:
                        if verbose is False:
                            print(kanji, "=", x)
                        else:
                            jisho[kanji]()
                    elif hiragana in jisho[kanji].kunyomi:
                        if verbose is False:
                            print(kanji, "->", hiragana)
                        else:
                            jisho[kanji]()
                    elif katakana in jisho[kanji].onyomi:
                        if verbose is False:
                            print(kanji, "~>", katakana)
                        else:
                            jisho[kanji]()


def show_all(jisho):
    """Shows all kanji in the dictionary"""
    for kanji in jisho:
        jisho[kanji]()


def game(jisho, rounds):
    """Plays the random kanji game!"""
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

    print(">> You got " + str(correct) + " out of " + str(rounds)
          + " (" + str(100*correct/rounds) + "%)!\n")
