"""
    976. Largest Perimeter Triangle
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of 
    these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

    :type nums: List[int]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""

def largestPerimeter(self, nums):
    nums.sort(reverse = True)
    n=len(nums)
    for i in range(n-2):
        if nums[i]<nums[i+1]+nums[i+2]: return (nums[i]+nums[i+1]+nums[i+2])
    return 0