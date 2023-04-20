"""
        :type s: str
        :type t: str
        :rtype: bool
"""
def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram("anagram","nagaram"))