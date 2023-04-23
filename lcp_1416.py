# 1416. Restore The Array
"""
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

Solution: DP
"""
class Solution:
    def numberOfArrays(self, s, k):
        n, mod = len(s), 10**9+7

        @lru_cache(None)
        def dfs(i):
            if i == 0:
                return 1

            total = 0

            for j in range(i-1,-1,-1):
                if s[j] == "0": continue
                elif int(s[j:i]) <= k:
                    total += dfs(j)%mod
                elif int(s[j:i]) > k:
                    break

            return total

        return dfs(n)%mod
