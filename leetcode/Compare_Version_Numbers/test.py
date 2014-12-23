import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.version1 = '0.1'
        self.version2 = '1.1'
        self.version3 = '1.2'
        self.version4 = '13.37'
        self.version5 = '13.37.0'

    def test_solution(self):
        self.assertEqual(self.solution.compareVersion(self.version1, self.version2), -1)
        self.assertEqual(self.solution.compareVersion(self.version2, self.version3), -1)
        self.assertEqual(self.solution.compareVersion(self.version4, self.version3), 1)
        self.assertEqual(self.solution.compareVersion(self.version4, self.version4), 0)
        self.assertEqual(self.solution.compareVersion(self.version4, self.version5), 0)

if __name__ == '__main__':
    unittest.main()