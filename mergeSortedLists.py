from ERRORMSGS import INVALID_K


def validKMergeLists(list1, list2, k):
    i, j = 0, 0

    count = 0
    while i < len(list1) and j < len(list2) and count < k:
        if list1[i] < list2[j]:
            yield list1[i]
            i = i + 1
        else:
            yield list2[j]
            j = j + 1

        count += 1

    while i < len(list1) and count < k:
        yield list1[i]
        i += 1
        count += 1

    while j < len(list2) and count < k:
        yield list2[j]
        j += 1
        count += 1


def mergeSortedLists(list1, list2, k):
    if k >= 0 and isinstance(k, int):
        return list(validKMergeLists(list1, list2, k))

    else:
        raise Exception(INVALID_K)
