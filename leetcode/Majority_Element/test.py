import unittest
from random import randint
from solution import Solution


class TestSolution(unittest.TestCase):

    def array_generator(self, n):
        """
        Generator an array with majority element 0

        :param n: the length of array
        """
        test = []
        threshold = n / 2 + 1
        for i in range(0, n-1):
            if i < threshold:
                test.append(0)
            else:
                test.append(randint(0, n))
        return test

    def setUp(self):
        self.hashtable = Solution.hashtable
        self.majority_voting = Solution.Boyer_Moore_Majority_Voting
        self.test = self.array_generator(100)

    def test_hashtable(self):
        self.assertEqual(self.hashtable(self.test), 0)

    def test_majority_voting(self):
        self.assertEqual(self.majority_voting(self.test), 0)


if __name__ == '__main__':
    unittest.main()
