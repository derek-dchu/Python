import unittest
from .solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test1 = "()[]{}"
        self.test2 = ")}{({))[{{[}"
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.isValid(self.test1))
        self.assertFalse(self.solution.isValid(self.test2))
        

if __name__ == '__main__':
    unittest.main()