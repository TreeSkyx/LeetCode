"""
        :type s: str
        :type t: str
        :rtype: str
"""
def findTheDifference(s, t):
    for i in t:
            if s.count(i) != t.count(i):
                return i
            
print(findTheDifference("abc","abcd"))
