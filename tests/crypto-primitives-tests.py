__author__ = 'Jonathan'

from primitives.frequency_analysis import FrequencyAnalysis

def setup():
    return None


def teardown():
    return None


def test_1():
    t = FrequencyAnalysis()
    print(t.get_alphabet())
    print(t.get_cmap())

