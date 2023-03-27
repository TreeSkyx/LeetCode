"""
    64. Minimum Path Sum
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
    which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    :type grid: List[List[int]]
    :rtype: int

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def minPathSum(self, grid):
        m,n = len(grid), len(grid[0])

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]

        for i in range(1,n):
            grid[0][i] += grid[0][i-1]

        for i in range(1,m):
             for j in range(1, n):
                  grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]