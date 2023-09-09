# 377. Combination Sum IV
"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

------------------------------------------------------------------------------------

Logic:
In-Depth, Step-by-Step Guide
Initialization and Base Case:

Create an array dp with target + 1 slots, each initialized to zero.
This array will serve as our memory storage where dp[i] represents the number of combinations that can sum up to i.
Now, set dp[0] to 1. This serves as the base case, representing that there is one way to reach the target sum of zero: by using zero itself.
Filling up the DP Array (Iterative Computation):

Start iterating from 1 up to target. For each i, the aim is to fill dp[i] with the number of combinations that can make up that sum.
To find dp[i], you need to look at the previously calculated dp values. How? For every number num in nums, you add dp[i - num] to dp[i] (given that i - num >= 0).
In simpler terms, for each i, you're summing up the number of ways to form i by looking at how you could have arrived at that sum using smaller numbers.
Reaching the Summit (Return the Result):

After the loop concludes, you've successfully built your pyramid. At its peak, dp[target] will hold the total number of combinations that make up the target sum.
Nuances of Time and Space Complexity
Time Complexity: O(N * target). The outer loop runs target times, and for each iteration, we potentially check all N numbers in nums.
Space Complexity: O(target). The array dp will have target + 1 elements, each requiring constant space. So the overall space complexity is linear in terms of the target value.
"""

# Program:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]
