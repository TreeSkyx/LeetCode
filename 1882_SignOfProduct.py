"""
    1822. Sign of the Product of an Array
    There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
    You are given an integer array nums. Let product be the product of all values in the array nums.
    Return signFunc(product).

    :type nums: List[int]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
from functools import reduce
from operator import mul
def arraySign(nums):
    return 1 if reduce(mul,nums) > 0 else 0 if reduce(mul,nums) == 0 else -1

print(arraySign([-1,-2,-3,-4,3,2,1]))