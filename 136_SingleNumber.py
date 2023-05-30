"""
    136. Single Number
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    :type nums: List[int]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def singleNumber(nums):
        uniqNum = 0
        for i in nums:
            uniqNum ^= i
        return uniqNum

print(singleNumber([4,1,2,1,2]))