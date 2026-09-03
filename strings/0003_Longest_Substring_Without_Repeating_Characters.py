# Problem: Longest Substring Without Repeating Characters
# LeetCode: 3
#
# Approach: Brute Force
# ---------------------
# Start from every character and extend the current substring
# until a repeated character is found. Keep the longest one.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        n = len(s)
        ans = ""

        for i in range(n - 1):
            a = str(s[i])

            for j in range(i + 1, n):
                if s[j] not in a:
                    a += s[j]
                else:
                    break

            if len(a) > len(ans):
                ans = a

        return len(ans)
