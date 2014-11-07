#!/usr/bin/python3

"""Main module; reads initial data"""

import os
import sys
from kanji import Kanji
from jisho import search

# Directory containing kanji files
DIR = sys.path[0] + "/data/"


def create_jisho(name, jisho):
    """Reads info about kanji in "name" file, creating a dictionary"""
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


# -------------------------------------------------------------------

jisho = {}

try:
    for txt in os.listdir(DIR):
        create_jisho(DIR + txt, jisho)
    search(jisho)

# Ctrl-C
except KeyboardInterrupt:
    print()
    exit(1)
