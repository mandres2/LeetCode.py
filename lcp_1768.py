"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
"""

# Solution:

"""
Approach: Two-Pointer

Create two variables, m and n, to store the length of word1 and word2.
Create an empty string variable result to store the result of merged words.
Create two pointers, i and j to point to indices of word1 and word2. We initialize both of them to 0.
While i < m || j < n:
If i < m, it means that we have not completely traversed word1. As a result, we append word1[i] to result. We increment i to point to next index of words.
If j < n, it means that we have not completely traversed word2. As a result, we append word2[j] to result. We increment j to point to next index of words.
Return results.
It is important to note how we form the result string in the following codes: - cpp: The strings are mutable in cpp, which means they can be changed. As a result, we used the string variable and performed all operations on it. It takes constant time to append a character to the string. - java: The String class is immutable in java. So we used the mutable StringBuilder to concatenate letters to result. - python: Strings are immutable in python as well. As a result, we used the list result to append letters and later joined the list with an empty string to return it as a string object. The join operation takes linear time equal to the length of results to merge results with empty string.

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)
