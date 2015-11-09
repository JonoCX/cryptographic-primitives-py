__author__ = 'Jonathan'


class FrequencyAnalysis:
    alphabet = None
    cMap = {}

    def __init__(self):
        self.alphabet = ['A', 'B', 'C', 'D',
                         'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X',
                         'Y', 'Z']
        self.populateMap(self)

    def get_alphabet(self):
        if self.alphabet is None:
            return None
        else:
            return self.alphabet

    def populate_map(self):
        dict((x, 0) for x in self.alphabet)
