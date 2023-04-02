"""
    704. Binary Search
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.

    :type nums: List[int]
    :type target: int
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def search(nums, target):
    lo = 0
    hi = len(nums) - 1

    while hi - lo > 1:
        mid = (hi + lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    if nums[lo] == target:
        return lo
    elif nums[hi] == target:
        return hi
    else:
        return -1
    
print(search([-1,0,3,5,9,12],2))