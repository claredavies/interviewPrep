def twoSum(nums, target):
    if len(nums) == 0:
        return None

    else:
        numsDict = {}
        for i in range(0, len(nums)):
            current = nums[i]
            pair = target - current

            if pair in numsDict:
                return [numsDict.get(pair), i]

            else:
                numsDict[current] = i
