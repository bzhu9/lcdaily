class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        grid.append([0 for i in range(len(grid[0]))])
        output = []

        def dfs(r, c):
            if len(grid) > r >= 0 and len(grid[0]) > c >= 0:
                if grid[r][c] == 0:
                    return c
                if grid[r][c] == 1 and len(grid[0]) - 1 > c and grid[r][c + 1] != -1:
                    return dfs(r + 1, c + 1)
                elif grid[r][c] == -1 and c > 0 and grid[r][c - 1] != 1:
                    return dfs(r + 1, c - 1)
            return -1
        for c in range(len(grid[0])):
            output.append(dfs(0, c))
        return output
