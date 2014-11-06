#!/usr/bin/python3

import sys
from kanji import Kanji

jisho = {}


def read_kanji(name):
    with open(name, "r") as _file:
        try:
            while True:
                data = []

                # Reads info about the kanji
                data.append(_file.readline().rstrip("\n"))
                data.append((_file.readline().rstrip("\n")).split(";"))
                data.append(int(_file.readline()))
                data.append((_file.readline().rstrip("\n")).split(";"))
                data.append((_file.readline().rstrip("\n")).split(";"))

                jisho[data[0]] = Kanji(data)
        except ValueError:
            pass


for _file in sys.argv[1:]:
    read_kanji(_file)

while True:
    x = input("Type in a kanji to search for it: ")
    if x in jisho:
        jisho[x]()
    else:
        print(x, "not found...")
