class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # grid 0 == water, 1 == land
        # assume edges are water
        # island are 1s connected

        # no island = 0
        # return max area so biggest island

        maxArea = 0

        visited = set()
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(row, col, visited, area):
            if row < 0 or col < 0 or row == ROW or col == COL or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))
            return (1 
            + dfs(row + 1, col, visited, area)
            + dfs(row - 1, col, visited, area)
            + dfs(row, col + 1, visited, area)
            + dfs(row, col - 1, visited, area))

        for row in range(ROW):
            for col in range(COL):
                if (row, col) not in visited and grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col, visited, 0))
        
        return maxArea
        