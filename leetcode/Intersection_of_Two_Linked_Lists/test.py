import unittest
from solution import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TestSolution(unittest.TestCase):

    def setUp(self):
        curr = ListNode('a1')
        self.headA = curr
        curr.next = ListNode('a2')
        curr = curr.next
        curr.next = ListNode('c1')
        curr = curr.next
        self.result = curr
        curr.next = ListNode('c2')
        curr = curr.next
        curr.next = ListNode('c3')
        curr = curr.next

        curr = ListNode('b1')
        self.headB = curr
        curr.next = ListNode('b2')
        curr = curr.next
        curr.next = ListNode('b3')
        curr = curr.next
        curr.next = self.result

        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.getIntersectionNode(self.headA, self.headB), self.result)

if __name__ == '__main__':
    unittest.main()

