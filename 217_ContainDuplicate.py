"""
        :type nums: List[int]
        :rtype: bool
"""
def containsDuplicate(nums):
    return len(set(nums))!=len(nums)

print(containsDuplicate([1,2,2,3]))