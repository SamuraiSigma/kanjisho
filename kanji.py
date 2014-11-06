SEPARATOR = " / "


class Kanji():

    def __init__(self, _data):
        data = list(_data)
        data.reverse()

        self._symbol = data.pop()
        self._meaning = data.pop()
        self._strokes = data.pop()
        self._kunyomi = data.pop()
        self._onyomi = data.pop()

    def __call__(self):
        print(self.symbol)
        print("Meaning:", SEPARATOR.join(self.meaning))
        print("Strokes:", str(self.strokes))
        print("Kunyomi:", SEPARATOR.join(self.kunyomi))
        print("Onyomi:", SEPARATOR.join(self.onyomi), "\n")

    @property
    def symbol(self):
        return self._symbol

    @property
    def meaning(self):
        return self._meaning

    @property
    def strokes(self):
        return self._strokes

    @property
    def kunyomi(self):
        return self._kunyomi

    @property
    def onyomi(self):
        return self._onyomi
