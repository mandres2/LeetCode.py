# 1312. Minimum Insertion Steps to Make a String Palindrome

"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Solution:
Recursion -> Top Down -> Bottom Up -> Bottom Up O(n)
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        def longestPalindromeSubseq(self, s: str) -> int:
            n = len(s)
            dp = [0] * n
            dpPrev = [0] * n

            for start in range(n - 1, -1, -1):
                dp[start] = 1
                for end in range(start + 1, n):
                    if s[start] == s[end]:
                        dp[end] = dpPrev[end - 1] + 2
                    else:
                        dp[end] = max(dpPrev[end], dp[end - 1])
                dpPrev = dp[:]

            return dp[n - 1]

        return len(s) - longestPalindromeSubseq(self, s)
