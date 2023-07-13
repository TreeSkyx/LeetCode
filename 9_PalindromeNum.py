"""
    9. Palindrome Number
    Given an integer x, return true if x is a palindrome, and false otherwise.

    :type x: int
    :rtype: bool

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def isPalindrome(self, x):
    x = str(x)
    count = 0
    for i in range(len(x)):
        if x[0-i] == x[i-1]:
            count += 1
    if count == len(x):
        return True
    else:
        return False
    
print(isPalindrome("",1000021))