"""
    67. Add Binary

    Given two binary strings a and b, return their sum as a binary string.

    :type a: str
    :type b: str
    :rtype: str
"""
def addBinary(self, a, b):
    return (bin(int(a,2)+(int(b,2)))[2:])

print(addBinary("","11","1"))