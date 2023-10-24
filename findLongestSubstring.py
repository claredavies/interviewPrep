def findLongestSubstring(s):
    if len(s) > 0:
        substring = [s[0]]
        list_sets = []

        set_count = 0
        for i in range(0, len(s) - 1):
            cur = s[i]
            next = s[i+1]

            if ord(cur) != ord(next):
                if next not in substring:
                    substring.append(next)
                else:
                    set_count += 1
                    list_sets.append(substring)
                    pos = substring.index(next)
                    substring = substring[(pos+1):]
                    substring.append(next)

            else:
                set_count += 1
                list_sets.append(substring)
                substring = [next]

        list_sets.append(substring)

        maxSet = max(list_sets, key= lambda s: len(s))
        return len(maxSet)

    else:
        return 0
