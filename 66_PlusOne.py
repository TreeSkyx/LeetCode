"""
    66. Plus One

    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

        :type digits: List[int]
        :rtype: List[int]
"""


def plusOne(self, digits):
    s = [str(i) for i in digits]
    num = int("".join(s)) + 1
    ans = []
    for i in str(num):
        ans.append(int(i))
    return(ans)
print(plusOne("",[9]))
