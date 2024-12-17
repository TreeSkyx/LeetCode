def islandPerimeter(grid):
        n = len(grid)
        m = len(grid[0])
        opt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (j > 0 and grid[i][j - 1] == 0) or j == 0:
                        opt += 1

                    if (i > 0 and grid[i - 1][j] == 0) or i == 0:
                        opt += 1

                    if (j < m - 1 and grid[i][j + 1] == 0) or j == m - 1:
                        opt += 1

                    if (i < n - 1 and grid[i + 1][j] == 0) or i == n - 1:
                        opt += 1
        return opt

    

print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))