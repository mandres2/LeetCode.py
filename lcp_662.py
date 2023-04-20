# 662. Maximum Width of Binary Tree
"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


Approach 1: BFS Traversal
Intuition

Naturally, one might resort to the BFS traversal. After all, the width is measured among the nodes on the same level. So let us get down to the BFS traversal first.

There are several ways to implement the BFS traversal. Almost all of them share a common point, i.e. using the queue data structure to maintain the order of visits.

In brief, we push the nodes into the queue level by level. As a result, the priorities of visiting would roll out from top to down and from left to right, due to the FIFO (First-In First-Out) principle of the queue data structure, i.e. the element that enters the queue first would exit first as well.

Algorithm

Here are a few steps to implement a solution with the BFS traversal.

First of all, we create a queue data structure, which would be used to hold elements of tuple as (node, col_index), where the node is the tree node and the col_index is the corresponding index that is assigned to the node based on our indexing schema. Also, we define a global variable called max_width which holds the maximal width that we've seen so far.

Then we append the root node along with its index 0, to kick off the BFS traversal.

The BFS traversal is basically an iteration over the elements of queue. We visit the nodes level by level until there are no more elements in the queue.

At the end of each level, we use the indices of the first and the last elements on the same level, in order to obtain the width of the level.
At the end of BFS traversal, we then return the maximal width that we've seen over all levels.

Time and Space Complexity: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0
        # queue of elements [(node, col_index)]
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width
