# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    solution for problem 'Leetcode: Intersection of Two Linked Lists'

    """
    def getIntersectionNode(self, headA, headB):
        """
        looking for the node at which the Intersection of two singly linked lists begins

        Returns:
            ListNode
        """

        if headA is None or headB is None:
            return None

        # Traverse A, count the number of nodes
        count_a = 0
        curr = headA
        while curr != None:
            count_a += 1
            curr = curr.next

        # Traverse B, count the number of nodes
        count_b = 0
        curr = headB
        while curr != None:
            count_b += 1
            curr = curr.next

        # Look for intersection
        diff_len = count_a - count_b

        currA = headA
        currB = headB
        if diff_len > 0:
            for i in range(0, diff_len):
                currA = currA.next

        elif diff_len < 0:
            for i in range(0, abs(diff_len)):
                currB = currB.next

        while currA != None:
            if currA is currB:
                return currA

            currA = currA.next
            currB = currB.next

        return None
