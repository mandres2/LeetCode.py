"""
2101. Detonate the Maximum Bombs

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

################################################################################

Approach: Breadth-First Search (BFS)

Algorithm:
Initialize answer as 0.

Create hash map graph containing all directed edges corresponding to the detonation relationships between all bombs.

Define a function bfs(i) that finds all the reachable nodes from node i.

Initialize an empty queue queue and an empty hash set visited.
Add i to both queue and visited.
While the queue is not empty, dequeue the fisrt node cur.
Check if cur has any unvisited neighbor nodes, if so, enqueue them into queue, add them to visited, and repeat the previous step.
Return the size of visited when the iteration is complete.
Call bfs on every node i and update answer as the maximum size of visited after each BFS.

Return answer when the all BFS operations are complete.

Time-Complexity: O(N^3)
Space-Complexity: O(N^2)
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)
        
        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]
                
                # Create a path from node i to node j, if bomb i detonates bomb j.
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
        
        def bfs(i):
            queue = collections.deque([i])
            visited = set([i])
            while queue:
                cur = queue.popleft()
                for neib in graph[cur]:
                    if neib not in visited:
                        visited.add(neib)
                        queue.append(neib)
            return len(visited)
        
        answer = 0
        for i in range(n):
            answer = max(answer, bfs(i))
        
        return answer
