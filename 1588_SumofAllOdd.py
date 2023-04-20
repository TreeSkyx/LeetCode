"""
    1588. Sum of All Odd Length Subarrays

    Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
    A subarray is a contiguous subsequence of the array.

    :type arr: List[int]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def sumOddLengthSubarrays(arr):
    ans=0
    for i in range(len(arr)):
        for j in range(i,len(arr),2):
            ans+=sum(arr[i:j+1])
    return ans

print(sumOddLengthSubarrays([1,4,2,5,3]))