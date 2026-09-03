# Problem: Longest Palindromic Substring
# LeetCode: 5
#
# Approach: Expand Around Center
# ------------------------------
# Treat every character and every gap between characters as a
# possible palindrome center. Expand outward while the characters
# match and keep the longest palindrome found.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = ""

        def expand(left, right, ans):
            while left >= 0 and right <= n:
                c = s[left:right]

                if c == c[::-1]:
                    ans = ans if len(c) <= len(ans) else c
                    left -= 1
                    right += 1
                else:
                    break

            return ans

        for i in range(n):
            ans = expand(i, i, ans)
            ans = expand(i, i + 1, ans)

        return ans
