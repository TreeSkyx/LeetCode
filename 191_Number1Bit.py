"""
    191. Number of 1 Bits
    Write a function that takes the binary representation of an unsigned integer and returns the 
    number of '1' bits it has (also known as the Hamming weight).

    :type n: int
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""

def hammingWeight(self, n):
    binary = format(n,'b')
    return binary.count('1')

n = int(input())
print(hammingWeight("",n))