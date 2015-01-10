class Solution:
    @staticmethod
    def hashtable(num):
        """
        Find the element that appears more the n/2 times

        Args:
            num: a list of integers
        
        Returns:
            an integer
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

    @staticmethod
    def Boyer_Moore_Majority_Voting(num):
        """
        O(n) runtime
        """
        # Initailize current_candidate and counter
        current_candidate = None
        counter = 0

        for n in num:
            if current_candidate is None:
                current_candidate = n
                counter = 1
            elif current_candidate == n:
                    counter += 1
            else:
                counter -= 1
                if counter == 0:
                    current_candidate = None
        return current_candidate