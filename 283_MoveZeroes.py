"""
    283. Move Zeroes
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.

    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] , nums[j] = nums[j], nums[i]
            i += 1