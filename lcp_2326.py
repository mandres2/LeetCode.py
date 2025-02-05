"""
LCP 2326: Spiral Matrix IV

Problem:
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.
Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
Return the generated matrix.

Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

Constraints:
1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000

Intuition
The problem requires us to fill a 2D matrix in a spiral order using the values from a singly linked list. The matrix starts with all elements initialized to -1, and as we traverse through the linked list, we replace the -1 values with the linked list values in a spiral order, starting from the top-left corner of the matrix.

The challenge lies in correctly navigating the matrix in a spiral pattern (right → down → left → up) and ensuring that we stay within the matrix boundaries without revisiting already filled positions. The key to solving this is to maintain a direction vector that changes whenever we encounter a boundary or a previously filled cell.

Approach
Initialize the Matrix:
Create a matrix of size m x n with all elements initialized to -1. This serves as our output matrix, where we will place the values from the linked list.

Set Up the Initial Conditions:
Start at the top-left corner of the matrix (r = 0, c = 0).
Define the direction vectors to facilitate spiral movement: right ((0,1)), down ((1,0)), left ((0,-1)), and up ((-1,0)).

Traverse the Linked List:
Begin iterating through the linked list. For each node, place its value in the current position of the matrix.
Calculate the next position based on the current direction. If the next position is within the matrix bounds and has not been visited (matrix[next_r][next_c] == -1), move to this position.
If the next position is either out of bounds or already filled, change direction by rotating the direction vector and update the position accordingly.

Termination:
Continue the process until the linked list is fully traversed. Any remaining positions in the matrix will remain -1, indicating they were not filled due to the linked list running out of values.

Return the Result:
Finally, return the filled matrix.

Complexity
Time complexity:
O(n)
Space complexity:
O(m * n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr=head
        matrix=[[-1] * n for _ in range(m)]
        r=0
        c=0
        d_p=0
        d=[(0,1),(1,0),(0,-1),(-1,0)]
        while curr:
            matrix[r][c]=curr.val
            curr=curr.next
            next_r,next_c=r+d[d_p%4][0],c+d[d_p%4][1]
            if 0<=next_r<m and 0<=next_c<n and matrix[next_r][next_c]==-1:
                r,c=next_r,next_c
            else:
                d_p+=1
                r,c=r+d[d_p%4][0],c+d[d_p%4][1]
        return matrix