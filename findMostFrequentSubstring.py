from collections import Counter


def findMostFrequentSubstring(substring, k):
    if isinstance(k, int) and k > 0:
        if len(substring) < k:
            return None

        elif len(substring) == k:
            return substring

        lis = []

        for i in range(0, (len(substring) - k + 1)):
            lis.append(substring[i:(i + k)])

        counted = Counter(lis)
        maxCount = max(counted.values())

        for key, val in counted.items():
            if val == maxCount:
                return key

    else:
        raise Exception("invalid k")
