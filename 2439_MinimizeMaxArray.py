"""
    2439. Minimize Maximum of Array
    You are given a 0-indexed array nums comprising of n non-negative integers.

    In one operation, you must:
    - Choose an integer i such that 1 <= i < n and nums[i] > 0.
    - Decrease nums[i] by 1.
    - Increase nums[i - 1] by 1.

    Return the minimum possible value of the maximum integer of nums after performing any number of operations.
    
    :type nums: List[int]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def minimizeArrayValue(nums):
    total_sum = 0
    result = 0
    for index in range(len(nums)):
        total_sum += nums[index]
        result = max(result, (total_sum + index) // (index + 1))
    return result

print(minimizeArrayValue([10,1]))