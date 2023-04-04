"""
    1790. Check if One String Swap Can Make Strings Equal
    You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two 
    indices in a string (not necessarily different) and swap the characters at these indices.

    Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. 
    Otherwise, return false.

    :type s1: str
    :type s2: str
    :rtype: bool

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def areAlmostEqual(s1, s2):
    if s1 == s2:
        return True
    elif sorted(s1) != sorted(s2):
        return False
    
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1

    if count != 2:
        return False
    return True

print(areAlmostEqual("bank","kanb"))