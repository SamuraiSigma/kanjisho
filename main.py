#!/usr/bin/python3

"""Main module; reads initial data and executes program"""

import os
import sys
import subprocess
import romkan
from kanji import Kanji

# Directory containing kanji files
DIR = sys.path[0] + "/data/"

# Global dict
jisho = {}


def read_kanji(name):
    """Reads info about kanji in "name" file"""
    with open(name, "r") as _file:
        i = 0
        data = []
        for line in _file:

            # Skips empty or commented lines
            if line == "\n" or line.startswith('#'):
                continue

            # Reads info about the kanji
            if i == 0:
                data.append(line.rstrip('\n'))
            elif i == 1 or i == 3 or i == 4:
                data.append((line.rstrip('\n')).split(';'))
            else:
                data.append(int(line))
            i += 1

            # Adds kanji to dict
            if i == 5:
                jisho[data[0]] = Kanji(data)
                del(data[:])
                i -= 5


def search():
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


# -------------------------------------------------------------------

try:
    for txt in os.listdir(DIR):
        read_kanji(DIR + txt)
    search()

# Ctrl-C
except KeyboardInterrupt:
    print()
    exit(1)
