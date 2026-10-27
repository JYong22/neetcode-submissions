class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2d grid where 1 is land and 0 is water
        #island is horizontal and vertical connected 1s and has water around the border. asume the edges are water


        # this is a dfs algo where we check up, down, left, right and see if whatever connects is land. 
        # if we visited we can assume that everything touching it has been visited because we run a dfs on that
        

        # lets get the grid
        ROW = len(grid)
        COL = len(grid[0])

        # visited set to see what blocks we have been. It can be a set because only 1 instance of a grid
        visited = set()
        total_islands = 0

        # lets make the helper dfs
        def dfs(row, col, visited):
            nonlocal total_islands
            # lets make a base case. This is to make sure we exit so edges, water, or visited
            if row < 0 or col < 0 or row == ROW or col == COL or (row, col) in visited or grid[row][col] == "0":
                return;
            
            visited.add((row, col))
            # check around
            dfs(row + 1, col, visited)
            dfs(row - 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)




        #lets loop through the grid
        for row in range(ROW):
            for col in range(COL):
                # if we haven't seen we should go through it has to be land for obvious reasons
                if (row, col) not in visited and grid[row][col] == "1":
                    total_islands +=1
                    dfs(row, col, visited)
        
        return total_islands
