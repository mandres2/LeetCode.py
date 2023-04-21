# 879. Profitable Schemes

"""
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).



Approach: DP
Time and space complexity: O(n)^2
"""
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m=len(group)
        dp=[[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        for j in range(n+1):
            dp[m][j][0]=1

        for i in range(m-1,-1,-1):
            for j in range(n+1):
                for k in range(minProfit+1):
                    dp[i][j][k]=dp[i+1][j][k]
                    if group[i]<=j:
                        dp[i][j][k]+=dp[i+1][j-group[i]][max(0,k-profit[i])]
                    dp[i][j][k]%=10**9+7

        return dp[0][n][minProfit]         
