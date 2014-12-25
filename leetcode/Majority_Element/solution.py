class Solution:
    def majorityElement(self, num):
        """
        Find the element that appears more the n/2 times

        :param: num, a list of integers
        :return: an integer
        """
        if len(num) == 1:
            return num[0]

        majority_count = len(num) / 2 + 1
        majority = dict()

        for n in num:
            if majority.has_key(n):
                majority[n] += 1
                if majority[n] == majority_count:
                    return n
            else:
                majority[n] = 1