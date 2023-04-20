"""
    1672. Richest Customer Wealth

    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​th​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
    A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

    :type accounts: List[List[int]]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def maximumWealth(accounts):
    return max([sum(acc) for acc in accounts])

print(maximumWealth([[1,2,3],[3,2,1]]))