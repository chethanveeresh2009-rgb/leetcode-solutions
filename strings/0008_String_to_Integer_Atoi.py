# Problem: String to Integer (atoi)
# LeetCode: 8
#
# Approach: Parse Characters
# --------------------------
# Skip leading spaces, read an optional sign, then process digits
# one by one. Stop at the first non-digit and clamp the result to
# the signed 32-bit integer range.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        res = 0
        idx = 0
        n = len(s)

        while idx < n and s[idx] == " ":
            idx += 1

        if idx < n and (s[idx] == "+" or s[idx] == "-"):
            if s[idx] == "-":
                sign = -1
            idx += 1

        while idx < n and '0' <= s[idx] <= '9':
            digit = ord(s[idx]) - ord('0')
            res = res * 10 + digit

            if res > 2**31 - 1:
                return (2**31 - 1) if sign == 1 else (-2**31)

            idx += 1

        return res * sign
