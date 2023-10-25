import pytest

from findMostFrequentSubstring import findMostFrequentSubstring


def test_findMostFrequentSubstringValid():
    s = "inengineering"
    res = findMostFrequentSubstring(s, 2)
    assert res == "in"


# invalid k - not int

# invalid k - negative

# k MORE than string
def test_findMostFrequentSubstringValid():
    s = "inengineering"
    res = findMostFrequentSubstring(s, 2)
    assert res == "in"

    s = "boxjdjdjdboxddd"
    res = findMostFrequentSubstring(s, 3)
    assert res == "box"

    s = "sssblahsssblahblah"
    res = findMostFrequentSubstring(s, 3)
    assert res == "bla"

    res = findMostFrequentSubstring(s, 4)
    assert res == "blah"

    res = findMostFrequentSubstring(s, 1)
    assert res == "s"


# make sure to check start and end!!!!

# k is equal to the string
def test_findMostFrequentSubstringKEqualString():
    s = 'ssb'
    k = 3
    res = findMostFrequentSubstring(s, k)
    assert res == 'ssb'


def test_findMostFrequentSubstringStringEmpty():
    s = []
    k = 3
    res = findMostFrequentSubstring(s, k)
    assert res == None


def test_findMostFrequentSubstringKInvalid():
    s = []
    k = -1

    with pytest.raises(Exception):
        findMostFrequentSubstring(s, k)

    k = 1.11
    with pytest.raises(Exception):
        findMostFrequentSubstring(s, k)

# when multiple answers - take the first one???
