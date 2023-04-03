"""
    1502. Can Make Arithmetic Progression From Sequence
    A sequence of numbers is called an arithmetic progression if the difference between any two c
    onsecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. 
    Otherwise, return false.

    :type arr: List[int]
    :rtype: bool

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def canMakeArithmeticProgression(arr):
    arr = sorted(arr)
    dif = arr[1] - arr[0]
    for i in range(1,len(arr)-1):
        if arr[i+1] - arr[i] != dif:
            return False
    return True

print(canMakeArithmeticProgression([3,5,1]))