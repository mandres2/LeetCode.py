'''
The algorithm is simple as follows

Traverse the grid block by block
If the block is land increment perimeter by 4 and check it's top and left neighbours. If the neighbours are land blocks decrement perimeter by 2 per intersection.
Repeat the process until the whole grid is traversed
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m , n = len(grid) , len(grid[0]) 
        def has_neighbors(i,j):
            p = 4
            for a,b in [[1,0],[0,1],[-1,0],[0,-1]]:
                if (0 <= i+a < m) and (0 <= j+b < n):
                    if grid[i+a][j+b] == 1:
                        p -= 1
            return p if p > 0 else 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += has_neighbors(i,j)
        return perimeter