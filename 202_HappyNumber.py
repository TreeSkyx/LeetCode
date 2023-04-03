"""
    202. Happy Number
    Write an algorithm to determine if a number n is happy.
    
    A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    :type n: int
    :rtype: bool

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""

def isHappy(n):
    n = str(n)
    b = 0
    for j in range(7):
        for i in n:
            b+=int(i)**2
        if b==1:
            return True
        else:
            n = str(b)
            b = 0
    return False


print(isHappy(2))