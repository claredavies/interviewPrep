from findLongestSubstring import findLongestSubstring


def test_findLongestSubstringOneLetter():
    res = findLongestSubstring("sssss")
    assert res == 1


def test_findLongestSubstringMixLetters():
    res = findLongestSubstring("abcabc")
    assert res == 3


def test_findLongestSubstringExample2():
    res = findLongestSubstring("pwwkew")
    assert res == 3


def test_findLongestSubstringExample3():
    res = findLongestSubstring("pwwkew")
    assert res == 3


def test_findLongestSubstringExample4():
    res = findLongestSubstring("aab")
    assert res == 2


def test_findLongestSubstringExample5():
    res = findLongestSubstring("ckilbkd")
    assert res == 5


def test_findLongestSubstringExample6():
    res = findLongestSubstring("dvdf")
    assert res == 3


def test_findLongestSubstringExample7():
    res = findLongestSubstring("anviaj")
    assert res == 5


def test_findLongestSubstringEmpty():
    res = findLongestSubstring("")
    assert res == 0

    # "aab"
