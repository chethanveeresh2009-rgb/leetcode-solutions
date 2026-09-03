# Problem: Reverse Integer
# LeetCode: 7
#
# Approach: Digit Extraction
# --------------------------
# Extract the last digit repeatedly and build the reversed number.
# Apply the original sign at the end and return 0 if the result
# falls outside the signed 32-bit integer range.
#
# Time Complexity: O(log10(x))
# Space Complexity: O(1)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        if rev > 2**31 - 1:
            return 0

        return rev * sign
