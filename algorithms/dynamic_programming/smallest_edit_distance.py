"""
Suppose that we want to transform the word "algorithm"
into the word "alligator". For each letter we can
either copy the letter from one word to anther at a cost
of 5, we can delete a letter at cost of 20, or insert
a letter at a cost of 20. We are looking the smallest
distance (lowest cost) between any two words.
"""
def solution(word1, word2):
    """
    Find the smallest distance between two words.

    algorithm:
        define:
            m[i, j] = d(s1[1..i], s2[i..j])
            l1 = length of s1
            l2 = length of s2

        we have:
            m[0, 0] = 0
            m[i, 0] = i * 20, i=1..l1
            m[0, j] = j * 20, j=1..l2

        for i:= 0 to l1
            for j:= 0 to l2
                m[i, j] = min(
                    m[i-1, j-1] + if s1[i] == s2[j] then 5 else 20,
                    m[i-1, j] + 20,
                    m[i, j-1] + 20
                    ), i=1..l1, j=1..l2

        return m[l1, l2]

    :param word1: string of word one
    :param word2: string of word two

    :return: an integer represent the cost
    """
    l1 = len(word1) + 1
    l2 = len(word2) + 1
    cache = matrix = [[0 for j in range(l2)] for i in range(l1)]

    for i in range(1, l1):
        cache[i][0] = i * 20
    for j in range(1, l2):
        cache[0][j] = j * 20
    for i in range(1, l1):
        for j in range(1, l2):
            if word1[i-1] != word2[j-1]:
                cost = 20
            else:
                cost = 5

            cache[i][j] = min(
                cache[i-1][j-1] + cost,
                cache[i-1][j] + 20,
                cache[i][j-1] + 20
                )
                
    return cache[-1][-1]


if __name__ == '__main__':
    word1 = "algorithm"
    word2 = "alligator"

    print solution(word1, word2)

