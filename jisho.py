"""User-dictionary interaction functions are here"""

import sys
import subprocess
import romkan
from kanji import Kanji


def search(jisho):
    """Dictionary mode, where kanji previously read can be searched"""
    while True:
        x = input("Type in something to search for it: ")

        if x.startswith('%'):
            x = romkan.to_hiragana(x[1:])

        if x.startswith('@'):
            x = romkan.to_katakana(x[1:])

        if x == "#exit":
            break

        elif x == "#all":
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

        elif x == "#clear":
            clear_screen()

        elif x in jisho:
            jisho[x]()

        else:
            for kanji in jisho:
                if x in jisho[kanji].meaning:
                    print(kanji, "=", x)
                elif x in jisho[kanji].kunyomi:
                    print(kanji, "->", x)
                elif x in jisho[kanji].onyomi:
                    print(kanji, "~>", x)


def clear_screen():
    """Uses the 'clear' option from the OS"""
    if sys.platform == "linux":
        subprocess.call("clear")
    elif sys.platform == "win32":
        subprocess.call("cls", shell=True)
