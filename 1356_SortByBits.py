"""
        :type arr: List[int]
        :rtype: List[int]
"""


def sortByBits(arr):
    return sorted(sorted(arr), key=lambda x: bin(x).count('1'))

print(sortByBits([0,1,2,3,4,5,6,7,8]))