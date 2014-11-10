#!/usr/bin/python3

"""Main module; reads initial data"""

import os
import sys
from kanji import Kanji
from jisho import search

# Directory containing kanji files
DIR = sys.path[0] + "/../data/"
ERROR = "Error when reading"


def create_jisho(name, jisho):
    """Reads info about kanji in "name" file, creating a dictionary"""
    with open(name, "r") as _file:
        i = 0
        data = []
        for line in _file:

            # Skips empty or commented lines
            if line == "\n" or line.startswith('#'):
                continue

            # Reads info about the kanji; stops if an error is found
            try:
                if i == 0:
                    data.append(line.rstrip('\n'))
                elif i in (1, 3, 4):
                    data.append((line.rstrip('\n')).split(';'))
                else:
                    data.append(int(line))
                i += 1
            except ValueError:
                print(ERROR, name)
                return

            # Adds kanji to dict
            if i == 5:
                jisho[data[0]] = Kanji(data)
                del(data[:])
                i -= 5


def usage():
    """Shows how to use the program and leaves it"""
    print("Usage:\n\t%s [-a] [-g<NUMBER>] [-v] [-h]" % sys.argv[0])
    print("-a: Shows all kanji")
    print("-g<NUMBER>: Plays NUMBER rounds of a kanji game, NUMBER > 0")
    print("-v: Verbose mode (shows all info about a searched kanji)")
    print("-h: Shows how to use the program and leaves it")
    exit(1)


# -------------------------------------------------------------------

# Command line argument variables
show_all = verbose = False
game_rounds = 0

for arg in sys.argv[1:]:
    if arg == "-h":
        usage()
    elif arg == "-a":
        show_all = True
    elif arg.startswith("-g"):
        game_rounds = int(arg[2:])
    elif arg == "-v":
        verbose = True

jisho = {}  # Kanji dictionary

try:
    for txt in os.listdir(DIR):
        create_jisho(DIR + txt, jisho)
    search(jisho, show_all, game_rounds, verbose)

# Ctrl-C
except KeyboardInterrupt:
    print()
    exit(1)
