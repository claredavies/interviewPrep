from twoSum import twoSum


def test_twoSumEmptyArray():
    nums = []
    target = 5
    res = twoSum(nums, target)
    assert res == None


def test_twoSumHappyPathStartIndex():
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums, target)
    assert res == [0, 1]


def test_twoSumHappyPathEndIndex():
    nums = [3, 2, 4]
    target = 6
    res = twoSum(nums, target)
    assert res == [1, 2]


def test_twoSumHappyPathSame2Values():
    nums = [3, 3]
    target = 6
    res = twoSum(nums, target)
    assert res == [0, 1]
