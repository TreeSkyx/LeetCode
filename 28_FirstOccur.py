"""
    28. Find the Index of the First Occurrence in a String

    Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    :type haystack: str
    :type needle: str
    :rtype: int
"""
def strStr(self, haystack, needle):
        return haystack.find(needle)

print(strStr("", "leetcode","leeto"))