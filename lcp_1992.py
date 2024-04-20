'''
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

Intuition
This kind of grid land/water problems usually can be solved via graph traversal, but is there a way to make it more space efficient than BFS or DFS which usually require O(n) space for queue or stack?

Approach
The main insight is that the farmland groups must always be a rectangle - we can use this property to just track till where the rectangle expands. We then mark the farmland as visited/forestland to not explore the rectangle from it again.

Complexity
Time complexity:
O(rows*cols)

Space complexity:
O(1)
'''

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        res = []

        def expand_from(i, j):
            # expand a rectangle of farmland starting from (i, j) as much as possible
            bottom, right = i, j
            while bottom + 1 < rows and land[bottom + 1][j] == 1:
                bottom += 1
            while right + 1 < cols and all(land[k][right + 1] == 1 for k in range(i, bottom + 1)):
                right += 1
            
            # mark farmland as visited
            for x in range(i, bottom + 1):
                for y in range(j, right + 1):
                    land[x][y] = 0  

            res.append([i, j, bottom, right])

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:  
                    expand_from(i, j)

        return res

