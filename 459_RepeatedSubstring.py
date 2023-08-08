"""
    459. Repeated Substring Pattern

    Given a string s, 
    check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

    :type s: str
    :rtype: bool
"""

def repeatedSubstringPattern(self, s):
    return True if s in (s+s)[1:-1] else False

print(repeatedSubstringPattern("", "aba"))