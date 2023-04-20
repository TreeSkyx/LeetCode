"""
    1572. Matrix Diagonal Sum
    Given a square matrix mat, return the sum of the matrix diagonals.
    Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

    :type mat: List[List[int]]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def diagonalSum(mat):
    ans = 0
    n = len(mat)
    for i in range(n):
        ans += mat[i][i]
        ans += mat[i][n-i-1]
    if n%2 == 1:
        ans -= mat[n//2][n//2]
    return ans

print(diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))