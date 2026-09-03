# Problem: Median of Two Sorted Arrays
# LeetCode: 4
#
# Approach: Merge and Sort
# ------------------------
# Combine both arrays into one list, sort it, and then find
# the middle element(s) to calculate the median.
#
# Time Complexity: O((n + m) log(n + m))
# Space Complexity: O(n + m)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = nums1 + nums2
        x.sort()

        n = len(x)
        m = n // 2

        if n % 2 == 0:
            return (x[m] + x[m - 1]) / 2.0
        else:
            return x[m]
