"""
    896. Monotonic Array

    An array is monotonic if it is either monotone increasing or monotone decreasing.
    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic, or false otherwise.

    :type nums: List[int]
    :rtype: bool
"""

def isMonotonic(self, nums):
    inc = True
    dec = True
    for i in range (len(nums)-1):
        if nums[i] > nums[i+1]:
            inc = False
        if nums[i] < nums[i+1]:
            dec = False
    return dec or inc
        
            
print(isMonotonic("",[1,1,2,3]))
                  