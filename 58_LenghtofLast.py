"""
    58. Length of Last Word

    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substringconsisting of non-space characters only.

    :type s: str
    :rtype: int
"""

def lengthOfLastWord(self, s):
    s = s.split()
    return len(s[len(s)-1])

print(lengthOfLastWord("","luffy is still joyboy"))