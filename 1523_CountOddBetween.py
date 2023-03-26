"""
    1523. Count Odd Numbers in an Interval Range
    Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

    :type low: int
    :type high: int
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""

def countOdds(self, low, high):
    odd = (high-low) // 2
    if low%2 == 1 or high%2 == 1:
        odd+=1  
    return odd

low = int(input("low = "))
high = int(input("high = "))
print(countOdds('',low,high))

