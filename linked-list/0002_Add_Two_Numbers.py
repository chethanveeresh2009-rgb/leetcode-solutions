# Problem: Add Two Numbers
# LeetCode: 2
#
# Approach: Linked List Addition
# ------------------------------
# Traverse both linked lists together, add corresponding digits,
# and keep track of the carry. A dummy node makes construction
# of the result list straightforward.
#
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m)) for the result list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        ans = dummy
        t = dummy
        t1 = l1
        t2 = l2
        carry = 0

        while t1 or t2:
            x = t1.val if t1 else 0
            y = t2.val if t2 else 0

            a = x + y + carry
            digit = a % 10
            carry = a // 10

            t.next = ListNode(digit)
            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
            t = t.next

        if carry > 0:
            t.next = ListNode(carry)

        return ans.next
