def reduce(c1, c2):
    for c in ['a', 'b', 'c']:
        if c not in {c1, c2}:
            return c

cache = {
    'min_len': -1
}

def helper(str):
        global cache

        if len(str) == 2:
            if str[0] == str[1]:
                return 2
            return 1

        if str in cache:
            return cache[str]

        cur_min_len = len(str)
        for i in range(0, len(str)-1):
            if str[i] != str[i+1]:
                min_len = helper(str[:i] + reduce(str[i], str[i+1]) + str[i+2::])
            else:
                min_len = len(str)
            if min_len < cur_min_len:
                cur_min_len = min_len
        cache[str] = cur_min_len
        return min_len

def StringReduction(str):
    if str is None:
        return None

    helper(str)
    return cache[str]


"""
class StringReduction:
    def __init__(self):
        self.min_len = -1

    def helper(self, str, length):
        if len(str) == 1:
            if length < self.min_len:
                self.min_len = length

        for i in range(0, len(str)-1):
            if str[i] != str[i+1]:
                self.helper(str[:i] + reduce(str[i], str[i+1]) + str[i+2::], length-1)
            self.helper(str[0:i] + str[i+1::], length)

    def string_reduction(self, str):
        self.min_len = len(str)
        self.helper(str, len(str))
        return self.min_len
"""
    

if __name__ == '__main__':
    def assertion(str, expected_min_len):
        assert(StringReduction(str) == expected_min_len), "Fail. str: {} ({}), expected: {}".format(str, StringReduction(str), expected_min_len)

    assertion(None, None)
    assertion("aaa", 3)
    assertion("abcabc", 2)
    assertion("aaabcb", 1)