import pytest

from ERRORMSGS import INVALID_K
from mergeSortedLists import mergeSortedLists


def test_mergedSortedListsSameLengthTest():
    list1 = [3, 4, 6]
    list2 = [1, 8, 10]
    result = mergeSortedLists(list1, list2, len(list1) + len(list2))
    assert result == [1, 3, 4, 6, 8, 10]


def test_mergedSortedListsList1Empty():
    list1 = []
    list2 = [2, 4, 5]
    result = mergeSortedLists(list1, list2, len(list1) + len(list2))
    assert result == [2, 4, 5]


# list 2 empty
def test_mergedSortedListsList2Empty():
    list1 = [3, 6, 12, 19]
    list2 = []
    result = mergeSortedLists(list1, list2, len(list1) + len(list2))
    assert result == [3, 6, 12, 19]


def test_mergedSortedListsList1Bigger():
    list1 = [3, 6, 12, 19, 34]
    list2 = [1, 16]
    result = mergeSortedLists(list1, list2, len(list1) + len(list2))
    assert result == [1, 3, 6, 12, 16, 19, 34]


def test_mergedSortedListsList2Bigger():
    list1 = [1, 16]
    list2 = [3, 6, 12, 19, 34]

    result = mergeSortedLists(list1, list2, len(list1) + len(list2))
    assert result == [1, 3, 6, 12, 16, 19, 34]


def test_mergeSortedListsLimitedK():
    list1 = [1, 16]
    list2 = [3, 6, 12, 19, 34]

    result = mergeSortedLists(list1, list2, 1)
    assert result == [1]

    result = mergeSortedLists(list1, list2, 3)
    assert result == [1, 3, 6]

    result = mergeSortedLists(list1, list2, 5)
    assert result == [1, 3, 6, 12, 16]


# experiment with k
def test_mergedSortedListsKZero():
    list1 = [1, 16]
    list2 = [3, 6, 12, 19, 34]

    result = mergeSortedLists(list1, list2, 0)
    assert result == []


def test_mergedSortedListsKNotInt():
    list1 = [1, 16]
    list2 = [3, 6, 12, 19, 34]

    with pytest.raises(Exception) as execinfo:
        mergeSortedLists(list1, list2, 1.11)
    assert str(execinfo.value) == INVALID_K


def test_mergedSortedListsKNegative():
    list1 = [1, 16]
    list2 = [3, 6, 12, 19, 34]

    with pytest.raises(Exception) as execinfo:
        mergeSortedLists(list1, list2, -1)
    assert str(execinfo.value) == INVALID_K
