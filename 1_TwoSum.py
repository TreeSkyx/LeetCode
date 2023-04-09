"""
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i!=j:
                return [i,j]
            
print(twoSum([2,7,11,15],9))