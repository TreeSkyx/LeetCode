"""
    1281. Subtract the Product and Sum of Digits of an Integer
    Given an integer number n, return the difference between the product of its digits and the sum of its digits.

    :type n: int
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def subtractProductAndSum(self, n):
    prod = 1
    sum = 0
    while n>0:
        digit = n % 10
        sum += digit
        prod *= digit
        n = n//10
    return int(prod - sum)

n = int(input())
print(subtractProductAndSum("",n))